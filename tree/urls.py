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

# urls for external applications:
urlpatterns = [
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls,name = 'adm'),
    url(r'^plot/', include('plot.urls')),
    url(r'^hw1/', include('hw1.urls')),
    url(r'^lua/', include('lua.urls')),
    # url(r'^contacts/', include('contacts.urls')),

# # urls for the initial part app
    url(r'^$', 'app.views.home', name='home'),
    url(r'^query$', 'app.views.query', name='query'),
    url(r'^questions$', 'app.views.questionnaire', name='questions'),
    url(r'^civil$', 'app.views.civil', name='civil'),   # To use the adresses directly

# # urls for the geolocation and cloud part lua
    url(r'^geolocation$', 'lua.views.geolocation', name='geolocation'),
        url(r'^cloud$', 'lua.views.cloud', name='cloud'),

# urls already installed
    url(r'^login/$',
        'django.contrib.auth.views.login',
        # 'login',
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
