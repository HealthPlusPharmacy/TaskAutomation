from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from api.api import v1

urlpatterns = [

    # Built-in django admin site
    url(r'^admin/', admin.site.urls),

    # Blank request
    url(r'^$', RedirectView.as_view(url='administration/login/')),

    # REST Api urls
    url(r'^api/', include(v1.urls)),

    # Administration app
    url(r'^administration/', include('administration.urls')),
]

