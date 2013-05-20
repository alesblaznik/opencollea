from django.conf.urls import patterns, include, url


urlpatterns = patterns("chat.views",
                       url("^$", "rooms", name="rooms"),
                       url("^(?P<slug>.*)$", "room", name="room"),
                       url("^create/$", "create", name="create"),
                       url("^system_message/$", "system_message",
                           name="system_message"),)
