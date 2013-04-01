from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from opencollea import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from portal import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "opencollea.views.home", name='home'),
    url(r'^courses', "opencollea.views.courses", name='courses'),
    url(r'^users', "opencollea.views.users", name='users'),
    url(r'^forums', "opencollea.views.forums", name='forums'),

    # Examples:
    # url(r'^$', 'opencollea.views.home', name='home'),
    # url(r'^opencollea/', include('opencollea.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Web portal.
    url(r'^portal/', include('portal.urls', namespace='portal')),

    # Serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': 'static'}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
