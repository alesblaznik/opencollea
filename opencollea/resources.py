from tastypie.resources import ModelResource
from opencollea.models import Course

class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'course'
