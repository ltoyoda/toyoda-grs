from django.shortcuts import render
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.template import loader, RequestContext
from django.views import generic
from datetime import datetime
from app.models import *


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'app/questions_edit.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app/results.html', {'question': question})


################################################################################

def questionnaire(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'app/questions.html', context_instance = RequestContext(request,
        {'title':'Questionnaire',
            'message':'Your application description page.',
            'year':datetime.now().year,}))


class IndexView(generic.ListView):
    template_name = 'app/questions.html'
 #       template_name = 'app/index_app.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
    #     """ Return the last five published questions (not including those set to be
    # published in the future)."""
         return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        # """Excludes any questions that aren't published yet. """
    #    return Question.objects.filter(pub_date__lte=timezone.now())

class DetailView(generic.DetailView):
    model = Question
    template_name = 'app/detail.html'
    def get_queryset(self):
        """        Excludes any questions that aren't published yet        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'app/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'app/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice, tente de novo!!!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app:results', args=(question.id,)))


##################################################################################
### *** Code for the second part

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'initial/index.html', context_instance = RequestContext(request,
        {'title':'Home Page',
            'year':datetime.now().year,}))

def grs(request):
    """Renders the home page: www.grs.citg.tudelft.nl """
    assert isinstance(request, HttpRequest)
    return render(request, 'initial/grs.html', context_instance = RequestContext(request,
        {'title':'Geoscience & Remote Sensing',
            'message':'TU Delft',
            'year':datetime.now().year,}))

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'initial/contact.html', context_instance = RequestContext(request,
        { 'title':'Contact Us',
            'message':'Your contact page.',
            'year':datetime.now().year,}))

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'initial/about.html', context_instance = RequestContext(request,
        {'title':'Luciana Toyoda',
            'message':'Your application description page.',
            'year':datetime.now().year,}))

def links(request):
    """Renders the links page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'initial/links.html',
        context_instance = RequestContext(request,
        {'title':'Links',
            'message':'Some useful links:',
            'year':datetime.now().year,}))


############################################################################
from django.shortcuts import render
from .models import PointOfInterest

# def poi_list(request):
#     pois = PointOfInterest.objects.all()
#     return render(request, 'app/poi_list.html', {'pois': pois})

def poi_list(request):
    """Renders the Google maps page."""
    pois = PointOfInterest.objects.all()
    assert isinstance(request, HttpRequest)
    return render(request,'initial/poi_list.html', context_instance = RequestContext(request,
        {'title':'Mapping the study area',
            'message':'Locating using coordinates.',
            'year':datetime.now().year,}))

def poi_list2(request):
    """Renders the Google maps page."""
    pois = PointOfInterest.objects.all()
    assert isinstance(request, HttpRequest)
    return render(request,'initial/poi_list2.html', context_instance = RequestContext(request,
        {'title':'Point of interest',
            'message':'Testing.',
            'year':datetime.now().year,}))

def poi_list2(request):
    """Renders the Google maps page."""
    pois = PointOfInterest.objects.all()
    assert isinstance(request, HttpRequest)
    return render(request,'initial/weather.html', context_instance = RequestContext(request,
        {'title':'Weather Information',
            'message':'Region: The Netherlands.',
            'year':datetime.now().year,}))


def poi_list_amir(request):
    """Renders Amir's map."""
    pois = PointOfInterest.objects.all()
    assert isinstance(request, HttpRequest)
    return render(request,'initial/poi_list_amir.html', context_instance = RequestContext(request,
        {'title':'Map',
            'message':'Your application description page.',
            'year':datetime.now().year,}))

def query(request):
    """Renders the example/template page."""
#     pois = PointOfInterest.objects.all()
    assert isinstance(request, HttpRequest)
    return render(request,'app/query.html',context_instance = RequestContext(request,
        {'title':'Initial Query',
            'message':'What would you like to do first?',
            'year':datetime.now().year,}))

def testando(request):
    """Renders the example/template page."""
#     pois = PointOfInterest.objects.all()
    assert isinstance(request, HttpRequest)
    return render(request,'app/testando.html',context_instance = RequestContext(request,
        {'title':'teste',
            'message':'testando?',
            'year':datetime.now().year,}))

def model(request):
    """Renders the example/template page."""
#     pois = PointOfInterest.objects.all()
    assert isinstance(request, HttpRequest)
    return render(request,'app/model.html',context_instance = RequestContext(request,
        {'title':'Template for new pages - change in app/views.py',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))


#####################################################################################
# # Simple views for the questionaire tree:
## Filhos
def B1(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/B1.html',context_instance = RequestContext(request,
        {'title':'Prospection',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))

def B2(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/B2.html',context_instance = RequestContext(request,
        {'title':'Natural Hazards',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))

def B3(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/B3.html',context_instance = RequestContext(request,
        {'title':'Soil Decomposition',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))

### Netos
def B1_a(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/B1_a.html',context_instance = RequestContext(request,
        {'title':'Oil',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))

def B1_b(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/B1_b.html',context_instance = RequestContext(request,
        {'title':'Gas',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))

def B1_c(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/B1_b.html',context_instance = RequestContext(request,
        {'title':'Mineral extraction',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))

##
def B2_a(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/B2_a.html',context_instance = RequestContext(request,
        {'title':'Landslides',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))

def B2_b(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/B2_b.html',context_instance = RequestContext(request,
        {'title':'Earthquakes',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))

def B2_c(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/B2_c.html',context_instance = RequestContext(request,
        {'title':'Volcanism',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))
##
def B3_a(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/B3_a.html',context_instance = RequestContext(request,
        {'title':'Question B3_a',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))

def B3_b(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/B3_b.html',context_instance = RequestContext(request,
        {'title':'Question B3_b',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))

def variogram_input(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/variogram_imput.html',context_instance = RequestContext(request,
        {'title':'variogram_imput B2',
            'message':'Your application description page - change in app/views.py',
            'year':datetime.now().year,}))
