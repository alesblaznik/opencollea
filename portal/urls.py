__author__ = 'Andraz'

from django.conf.urls import *
from portal.views import *

urlpatterns = patterns('',

    # Main web portal entrance.
    (r'^$', portal_main_page),

)
