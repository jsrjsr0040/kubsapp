"""kubsapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from notification.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #login(POST)
    url(r'^login/$', student_login),

    #check studentid(GET)
    url(r'^check_studentid/$', check_studentid),

    #sign up(POST)
    url(r'^signup/$', sign_up),

    #set_follow (POST)
    url(r'^follow/$', set_follow),

    #check_follow
    url(r'^get_follow/([0-9]{10})/$', get_follow),

    #check_profile
    url(r'^check_profile/([0-9]{10})/$', check_profile),

    #post_notice
    url(r'^post_notice/$', post_notice),

    #post_monthly_schedule
    url(r'^monthly_schedule/$', post_monthly_schedule),

    #post_daily_schedule
    url(r'^daily_schedule/$', post_daily_schedule),

    #get_specific_event
    url(r'^specific_event/$', get_specific_event),


]
