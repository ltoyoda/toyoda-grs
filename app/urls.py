"""tree URL Configuration

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

# app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index_app'),
    url(r'^questions$', views.index, name='questions'),
    # ex: /galho/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /galho/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/  # nao tem votos nesse app
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


    ### urls created for the questions
    url(r'^B1$', 'app.views.B1', name='B1'),
    url(r'^B2$', 'app.views.B2', name='B2'),
    url(r'^B3$', 'app.views.B3', name='B3'),

    url(r'^B1_a$', 'app.views.B1_a', name='B1_a'),
    url(r'^B1_b$', 'app.views.B1_b', name='B1_b'),
    url(r'^B1_c$', 'app.views.B1_c', name='B1_c'),

    url(r'^B2_a$', 'app.views.B2_a', name='B2_a'),
    url(r'^B2_b$', 'app.views.B2_b', name='B2_b'),
    url(r'^B2_c$', 'app.views.B2_c', name='B2_c'),
]