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
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_lua'),
    url(r'^irock$', views.irock, name='irock'),
    url(r'^geo$', views.geo, name='geo'),
    url(r'^geolocation$', views.geolocation, name='geolocation'),
        url(r'^geo_input_dist$', views.geo_input_dist, name='geo_input_dist'),
        url(r'^geo_distance$', views.geo_distance, name='geo_distance'),
        url(r'^cloud$', views.cloud, name='cloud'),
        url(r'^cloud_world$', views.cloud_world, name='cloud_world'),
        url(r'^cloud_world2$', views.cloud_world2, name='cloud_world2'),
        url(r'^cloud_world3$', views.cloud_world3, name='cloud_world3'),
        url(r'^agua$', views.agua, name='agua'),
]


#
# urlpatterns = patterns('',
# url(r'^$', views.index, name='index'))