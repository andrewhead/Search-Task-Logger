from django.conf.urls import url, include
from django.contrib import admin

from searchlogger.api import LocationEventResource


location_event_resource = LocationEventResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(location_event_resource.urls)),
]
