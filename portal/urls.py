from django.conf.urls import url, patterns
from portal import views

urlpatterns = patterns('',

    # Main web portal entrance.
    url(r'^$', views.main_page, name='main'),

    # Login / logout.
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', views.logout_page, name='logout'),

)
