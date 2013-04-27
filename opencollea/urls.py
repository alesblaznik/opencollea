from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from opencollea import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from tastypie.api import Api
from opencollea.resources import CourseResource
from opencollea import views

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(CourseResource())


urlpatterns = patterns('',
    url(r'^$', "opencollea.views.home", name='home'),
    url(r'^courses', "opencollea.views.courses", name='courses'),
    url(r'^users', "opencollea.views.users", name='users'),
    url(r'^forums', "opencollea.views.forums", name='forums'),

    # tole nevem kaj dela / ce sploh mora bit...
    url(r'^api/', include(v1_api.urls)),
    # Examples:
    # url(r'^$', 'opencollea.views.home', name='home'),
    # url(r'^opencollea/', include('opencollea.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Web portal.
    url(r'^portal/', include('portal.urls', namespace='portal')),

    # List of Mooc Courses
    url(r'^find_courses/', include('find_courses.urls',
                                   namespace='find_courses')),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
