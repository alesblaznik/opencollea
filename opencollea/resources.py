from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import request, request
from django.shortcuts import _get_queryset
from tastypie.authentication import SessionAuthentication
from tastypie.http import HttpUnauthorized, HttpForbidden
from tastypie.resources import ModelResource
from django.conf.urls import url
from tastypie.utils import trailing_slash

from opencollea.models import Course, UserProfile


class LoginResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth'
        excludes = ['email', 'password', 'is_superuser']
        #authentication = SessionAuthentication()

    def override_urls(self):
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

        data = self.deserialize(request, request.raw_post_data, format=request.META.get('CONTENT_TYPE', 'application/json'))

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
            return self.create_response(request, { 'success': True })
        else:
            return self.create_response(request, { 'success': False }, HttpUnauthorized)

    def current_user(self, request, **kwargs):
        user = {
            'id': request.user.id,
            'username': request.user.username,
        }
        return self.create_response(request, user)


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'course'


class UserProfileResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'user_profile'
