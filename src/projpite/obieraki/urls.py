from django.conf.urls import patterns, url, include
import os.path
from obieraki.views import *
from obieraki.forms import *
#admin.autodiscover()

urlpatterns = [
    url(r'^$', main_site),
    url(r'^index/$', main_site),
    url(r'^account/$', account_info),
    url(r'^courses/$', courses),
    url(r'^mycourses/$', mycourses),
    url(r'^register/$', register_page),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$',logout_page)
]
