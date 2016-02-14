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
#####################################
from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm



urlpatterns = [
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls,name = 'adm'),
####################################################################################
    url(r'^hw1/', include('hw1.urls')),
#    url(r'^hw2/', 'app.views.index_hw2',name='hw2'),

######################################################################################3
    url(r'^$', 'app.views.home', name='home'),
    url(r'^points$', 'app.views.poi_list', name='points'),

    url(r'^points_amir$', 'app.views.poi_list_amir', name='points_amir'),
    url(r'^testando$', 'app.views.testando', name='testando'),
    url(r'^model$', 'app.views.model', name='model'),
    url(r'^query$', 'app.views.query', name='query'),


    url(r'^grs$', 'app.views.grs', name='grs'),
    url(r'^links$', 'app.views.links', name='links'),

    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'initial/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
]
