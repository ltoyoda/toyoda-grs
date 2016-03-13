"""apk_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from . import views

#####################################
from datetime import datetime
# from plot.forms import BootstrapAuthenticationForm
from django.conf.urls import url
from . import views
from django.conf.urls import patterns, include, url
import contacts.views

urlpatterns = [
    # url(r'^$', views.contact_list, name='contact_list'),
    url(r'^$', contacts.views.ListContactView.as_view(),name='contacts-list'),
    url(r'^new$', contacts.views.CreateContactView.as_view(),name='contacts-new'),
]


