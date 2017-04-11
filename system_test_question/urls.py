# -*- coding: utf-8 -*-
"""system_test_question URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from USER_login import views as user_login_view


urlpatterns = [
    url(r'^$', user_login_view.home_page),
    url(r'^home_page.html', user_login_view.home_page),
    url(r'^register.html', user_login_view.register),
    url(r'^forget_password.html', user_login_view.forgot_password),
    url(r'^exercise_selection.html', user_login_view.exercise_selection),
    url(r'^exercise_write.html', user_login_view.exercise_write),
    url(r'^exercise_calculation.html', user_login_view.exercise_calculation),
    url(r'^admin/', admin.site.urls),
    url(r'^login.html', user_login_view.login_page),
    url(r'^logout', user_login_view.logout_page),
    url(r'^user_info', user_login_view.user_info),
]
