from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tastypie.authorization import Authorization
from tastypie.http import HttpUnauthorized
from tastypie.resources import ModelResource, ALL
from django.conf.urls import url
from tastypie.utils import trailing_slash
from tastypie import fields

from opencollea.models import Course, UserProfile, Question, EtherpadNote
from opencollea.forms import UserProfileForm, RegistrationDetailsForm, \
    EtherpadNoteForm, Answer, AnswerForm

from fixes.tastypie.validation import ModelCleanedDataFormValidation
import code_register.resources
from find_courses.models import Course as MoocCourse
from find_courses.resources import MoocCourseResource


class LoginResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth'
        excludes = ['email', 'password', 'is_superuser']
        #authentication = SessionAuthentication()

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login'), name="api_login"),
            url(r'^(?P<resource_name>%s)/logout%s$' %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('logout'), name='api_logout'),
            url(r'^(?P<resource_name>%s)/currentUser%s$' %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('current_user'), name='api_current_user'),
        ]

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        data = self.deserialize(request, request.raw_post_data,
                                format=request.META.get('CONTENT_TYPE',
                                                        'application/json'))

        username = data.get('username', '')
        password = data.get('password', '')
        redirect_to = data.get('redirectTo', '/')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return self.create_response(request, {
                    'success': True,
                    'redirectTo': redirect_to
                })
            else:
                return self.create_response(request, {
                    'success': False,
                    'reason': 'inactive',
                })
        else:
            return self.create_response(request, {
                'success': False,
                'reason': 'incorrect',
            })

    def logout(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        if request.user and request.user.is_authenticated():
            logout(request)
            return self.create_response(request, {'success': True})
        else:
            return self.create_response(request, {'success': False},
                                        HttpUnauthorized)

    def current_user(self, request, **kwargs):
        user = {
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
        }
        return self.create_response(request, user)


class UserProfileResource(ModelResource):
    courses_enrolled = fields.ToManyField(
        'opencollea.resources.CourseResource', 'courses_enrolled')
    language_code = fields.ForeignKey(
        code_register.resources.LanguageResource, 'language_code', null=True)
    age_range = fields.ForeignKey(
        code_register.resources.AgeRangeResource, 'age_range', null=True)
    gender = fields.ForeignKey(
        code_register.resources.GenderResource, 'gender', null=True)
    occupation = fields.ForeignKey(
        code_register.resources.OccupationResource, 'occupation', null=True)
    area_of_study = fields.ForeignKey(
        code_register.resources.AreaOfStudyResource,
        'area_of_study', null=True)

    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'user_profile'
        filtering = {
            'username': ALL,
        }
        excludes = ['password']
        authorization = Authorization()
        validation = ModelCleanedDataFormValidation(form_class=UserProfileForm)

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)"
                r"/courses_not_enrolled%s$"
                % (self._meta.resource_name,
                   trailing_slash()),
                self.wrap_view('get_courses_not_enrolled'),
                name="api_get_courses_not_enrolled"),
        ]

    def get_courses_not_enrolled(self, request, **kwargs):
        """
        Za uporabnika vrne razreda v katere ni vpisan.
        """
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        course_resource = CourseResource()
        objects = []
        for course in Course.objects.exclude(
                id__in=[c.id for c in UserProfile.objects.get
                        (pk=kwargs.get('pk', 0)).courses_enrolled.all()]
        ):
            bundle = course_resource.build_bundle(obj=course, request=request)
            bundle = course_resource.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)


class QuestionResource(ModelResource):
    # dostop preko foreignKey
    user = fields.ToOneField(UserProfileResource, 'user', full=True)
    answers = fields.ToManyField('opencollea.resources.AnswerResource',
                                 'answers', full=True)

    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'


class AnswerResource(ModelResource):
    user = fields.ToOneField(UserProfileResource, 'user', full=True)
    question = fields.ToOneField(QuestionResource, 'question')

    class Meta:
        queryset = Answer.objects.all()
        resource_name = 'answer'
        filtering = {
            'question': ALL,
        }
        ordering = ['id']
        authorization = Authorization()
        validation = ModelCleanedDataFormValidation(
            form_class=AnswerForm
        )


class CourseResource(ModelResource):
    questions = fields.ToManyField('opencollea.resources.QuestionResource',
                                   'questions', full=True)

    class Meta:
        queryset = Course.objects.all()
        resource_name = 'course'
        filtering = {
            'id': ALL,
            'machine_readable_title': ALL,
        }

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/new%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('new'), name="course_new"),
            url(r"^(?P<resource_name>%s)/mooc_courses_noone_took%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('mooc_courses_noone_took'),
                name="api_mooc_courses_noone_took"),
        ]

    def new(self, request, **kwargs):
        from opencollea.models import Course

        self.method_check(request, allowed=['post'])
        required = []
        data = self.deserialize(request, request.raw_post_data,
                                format=request.META.get('CONTENT_TYPE',
                                                        'application/json'))

        c = Course()
        c.title = data.get('title', '')  # required
        c.machine_readable_title = data.get('machine_readable_title', '')
        c.description = data.get('description', '')  # required
        c.website = data.get('website', '')

        if c.title == '':
            required.append('title')

        if c.description == '':
            required.append('description')

        if len(required) > 0:
            return self.create_response(request, {
                'required': required
            })
        else:
            c.save()

        #, machine_readable_title = d_machine_readable_title,
        # description = d_description, website = d_website
        if c.pk > 0:
            return self.create_response(request, {
                'success': True
            })
        else:
            return self.create_response(request, {
                'error': 'Entry not successful'
            })

    def mooc_courses_noone_took(self, request, **kwargs):
        """
        Mooc coursi iz katerih se ni narejenega nobenega "nasega" razreda.
        """
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        mooc_resource = MoocCourseResource()
        objects = []
        for mooc in MoocCourse.objects.exclude(
                pk__in=[c.mooc for c in
                        Course.objects.filter(mooc__isnull=False)]
        ):
            bundle = mooc_resource.build_bundle(obj=mooc, request=request)
            bundle = mooc_resource.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)


class RegistrationDetailsResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'registration_details'
        fields = ['first_name', 'last_name', 'email', 'password']
        authorization = Authorization()
        validation = ModelCleanedDataFormValidation(
            form_class=RegistrationDetailsForm)

    def dehydrate(self, bundle):
        # We don't send password to client
        bundle.data['password'] = ''

        return bundle


class EtherpadNoteResource(ModelResource):
    course = fields.ForeignKey(CourseResource, 'course')

    class Meta:
        queryset = EtherpadNote.objects.all()
        resource_name = 'etherpad_note'
        filtering = {
            'pad_id': ALL,
            'machine_readable_title': ALL,
            'course': ALL,
        }
        ordering = ['id']
        authorization = Authorization()
        validation = ModelCleanedDataFormValidation(
            form_class=EtherpadNoteForm
        )
