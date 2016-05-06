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
    url(r'^questions_edit$', views.index, name='questions_edit'),
    # url(r'^questions$', views.questionnaire, name='questions'),
    # ex: /galho/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /galho/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/  # nao tem votos nesse app
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

# urls for the initial part
    url(r'^points$', views.poi_list, name='points'),
    url(r'^points2$', views.poi_list2, name='points2'),
    url(r'^weather$', views.poi_list2, name='weather'),
    url(r'^points_amir$', views.poi_list_amir, name='points_amir'),
    url(r'^testando$', views.testando, name='testando'),
    url(r'^model$', views.model, name='model'),
    # url(r'^query$', views.query, name='query'),
    url(r'^grs$', views.grs, name='grs'),
    url(r'^links$', views.links, name='links'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about', views.about, name='about'),


    ### urls created for the questions
    url(r'^prospection$', views.prospection, name='prospection'),
    url(r'^natural$', views.natural, name='natural'),
    # url(r'^civil$', views.civil, name='civil'),
    url(r'^dams$', views.dams, name='dams'),
    url(r'^railways$', views.railways, name='railways'),
    url(r'^foundations$', views.foundations, name='foundations'),

    url(r'^oil$', views.oil, name='oil'),
    url(r'^gas$', views.gas, name='gas'),
    url(r'^mining$', views.mining, name='mining'),

    url(r'^landslides$', views.landslides, name='landslides'),
    url(r'^earthquakes$', views.earthquakes, name='earthquakes'),
    url(r'^volcanism$', views.volcanism, name='volcanism'),

    url(r'^sinkholes$', views.sinkholes, name='sinkholes'),
    url(r'^peat$', views.peat, name='peat'),
]