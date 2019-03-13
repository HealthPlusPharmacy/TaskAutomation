from django.conf.urls import url
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'administration'

urlpatterns = [

    # administration/
    url(r'^$', RedirectView.as_view(url='login/')),

    # administration/login/
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),

    # administration/logout/
    url(r'^log_out/$', auth_views.logout, {'next_page': 'administration:login'}, name='log_out'),

]