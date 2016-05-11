from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from django.http import HttpResponse, HttpRequest
from questions.models import *
from questions.compute import compute
from datetime import datetime
from . write import *
from questions.models import *
import os


def index(request):
    assert isinstance(request, HttpRequest)
    return render(request,'questions/first.html',context_instance = RequestContext(request,
        {'title':'Area of Interest',
            'message':'Your application description page - change in lua/views.py',
            'year':datetime.now().year,}))


def skygeo(request):
    assert isinstance(request, HttpRequest)
    return render(request,'questions/skygeo.html',context_instance = RequestContext(request,
        {'title':'Area of Interest',
            'message':'Your application description page - change in lua/views.py',
            'year':datetime.now().year,}))

# def index(request):
#     os.chdir(os.path.dirname(__file__))
#     result = None
#     if request.method == 'POST':
#         form = InputForm(request.POST)
#         if form.is_valid():
#             form2 = form.save(commit=False)
#             result = compute( form2.a, form2.b, form2.c, form2.d, form2.e, form2.f, form2.g, form2.h, form2.i, form2.file)
#             result = result.replace('static/', '')
#     else:
#         form = InputForm()
#
#     return render_to_response('questions/first.html',
#             {'form': form,
#              'result': result,
#              'title':'Railways questionnaire',
#              'message':'Questions - Variogram ',
#              'content': 'This is the text of the main page, here we can write whatever we want!!!....',
#
#              }, context_instance=RequestContext(request))

