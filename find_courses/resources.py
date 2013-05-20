from tastypie.resources import ModelResource
from find_courses.models import Course


class MoocCourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'mooc_course'
        allowed_methods = ['get']
