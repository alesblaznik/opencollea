from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from find_courses.models import Course

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
            queryset=Course.objects.all(),
            context_object_name='courses',
            template_name='find_courses/courses_list.html'),
        name='index')
)
