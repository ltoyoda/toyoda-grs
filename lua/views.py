from django.shortcuts import render
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.template import loader, RequestContext
from django.views import generic
from datetime import datetime
from lua.models import *




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'lua/index_lua.html', context)

def irock(request):
    assert isinstance(request, HttpRequest)
    return render(request,'lua/irock.html',context_instance = RequestContext(request,
        {'title':'irock',
            'message':'Your application description page - change in lua/views.py',
            'year':datetime.now().year,}))

def geo(request):
    assert isinstance(request, HttpRequest)
    return render(request,'lua/geo.html',context_instance = RequestContext(request,
        {'title':'geolocation',
            'message':'Your application description page - change in lua/views.py',
            'year':datetime.now().year,}))

def geolocation(request):
    assert isinstance(request, HttpRequest)
    return render(request,'lua/geolocation.html',context_instance = RequestContext(request,
        {'title':'geolocation',
            'message':'Your application description page - change in lua/views.py',
            'year':datetime.now().year,}))

def geo_input_dist(request):
    assert isinstance(request, HttpRequest)
    return render(request,'lua/geo_input_dist.html',context_instance = RequestContext(request,
        {'title':'geolocation',
            'message':'Your application description page - change in lua/views.py',
            'year':datetime.now().year,}))

def geo_distance(request):
    assert isinstance(request, HttpRequest)
    return render(request,'lua/geo_distance.html',context_instance = RequestContext(request,
        {'title':'geolocation',
            'message':'Your application description page - change in lua/views.py',
            'year':datetime.now().year,}))

def cloud(request):
    assert isinstance(request, HttpRequest)
    return render(request,'lua/cloud.html',context_instance = RequestContext(request,
        {'title':'Cloud Cover',
            'message':'Your application description page - change in lua/views.py',
            'year':datetime.now().year,}))

def agua(request):
    assert isinstance(request, HttpRequest)
    return render(request,'lua/agua.html',context_instance = RequestContext(request,
        {'title':'geolocation',
            'message':'Your application description page - change in lua/views.py',
            'year':datetime.now().year,}))

def cloud_world(request):
    assert isinstance(request, HttpRequest)
    return render(request,'lua/cloud_world.html',context_instance = RequestContext(request,
        {'title':'Cloud Cover',
            'message':'Your application description page - change in lua/views.py',
            'year':datetime.now().year,}))

def cloud_world2(request):
    assert isinstance(request, HttpRequest)
    return render(request,'lua/cloud_world2.html',context_instance = RequestContext(request,
        {'title':'Cloud Cover',
            'message':'Your application description page - change in lua/views.py',
            'year':datetime.now().year,}))

def cloud_world3(request):
    assert isinstance(request, HttpRequest)
    return render(request,'lua/cloud_world3.html',context_instance = RequestContext(request,
        {'title':'Cloud Cover',
            'message':'Your application description page - change in lua/views.py',
            'year':datetime.now().year,}))