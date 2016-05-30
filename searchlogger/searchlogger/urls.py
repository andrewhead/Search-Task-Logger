from django.conf.urls import url, include

from searchlogger.api import LocationEventResource


location_event_resource = LocationEventResource()

urlpatterns = [
    url(r'^api/', include(location_event_resource.urls)),
]
