from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

#########################################################################
from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from app.models import *


# def index(request):
#     return HttpResponse("Primeira resposta na tela, vai bem assim!!!.")
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('app/index_app.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# What will be shown in the screen is determined here:

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'app/index_app.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app/detail_app.html', {'question': question})

# This shows the results of the voting = need to be changed
def results(request, question_id):
    response = "Agora o resultado de cada uma   You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# Nao adicionar vote pra esse exemplo
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


##################################################################################

### Normal code
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'initial/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )


def grs(request):
    """Renders the GRS page."""  # http://www.citg.tudelft.nl/over-faculteit/afdelingen/geoscience-and-remote-sensing/
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'initial/grs.html',
        context_instance = RequestContext(request,
        {
            'title':'GRS Home Page',
            'year':datetime.now().year,
        })
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'initial/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'initial/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )


def links(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'initial/links.html',
        context_instance = RequestContext(request,
        {
            'title':'Links',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

############################################################################
from django.shortcuts import render
from .models import PointOfInterest

# def poi_list(request):
#     pois = PointOfInterest.objects.all()
#     return render(request, 'app/poi_list.html', {'pois': pois})

def poi_list(request):
    """Renders the about page."""
    pois = PointOfInterest.objects.all()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'initial/poi_list.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )