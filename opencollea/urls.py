from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from portal import views

admin.autodiscover()

urlpatterns = patterns('',
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
)
