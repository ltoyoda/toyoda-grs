from django.shortcuts import render
# from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.template import loader, RequestContext
# from django.views import generic
from datetime import datetime
# from plot.models import *
# from .models import Question

def home(request):
    assert isinstance(request, HttpRequest)
    return render(request,'plot/home_plot.html',context_instance = RequestContext(request,
        {'title':'In Construction!',
            'message':'Main home page! In apk_project!',
            'content': 'This is the text of the main page, here we can write whatever we want!!!....',
            'year':datetime.now().year,}))
#    return HttpResponse("Primeiro passo pra plotagem! says hello world!")

def index_plot(request):
    assert isinstance(request, HttpRequest)
    return render(request,'plot/plot.html',context_instance = RequestContext(request,
        {'title':'Home page of plot, inside apk_project!, In Construction!',
            'message':'Your application description page (index-index)- change in app/views.py',
            'content': 'This is the text of the main page, here we can write whatever we want!!!....',
            'year':datetime.now().year,}))
#    return HttpResponse("Primeiro passo pra plotagem! says hello world!")

def figures(request):
    assert isinstance(request, HttpRequest)
    return render(request,'plot/figures.html',context_instance = RequestContext(request,
        {'title':'Plotando',
            'message':'Your application description page (bor base-B1)- change in app/views.py',
            'content': 'This is the text of the page, here we can write quite a lot....',
            'year':datetime.now().year,}))

def plotando(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'plot/plotando.html', context_instance = RequestContext(request,
        {'title':'Extra page to test PLOTS',
            'message':'Your application description page (bor base-B1)- change in app/views.py',
            'content': 'This is the text of the page, here we can write quite a lot....',
            'year':datetime.now().year,}))


def text_output(request):
#    return HttpResponse("<strong>    ...In Construction! <strong>")
    assert isinstance(request, HttpRequest)
    return render(request,'plot/txt.html',context_instance = RequestContext(request,
        {'title':'    ...In Construction!',
            'message':'Your application description page - change in app/views.py',
            'content': 'This is the text of the main page, here we can write whatever we want!!!....',
            'year':datetime.now().year,}))

# ##############################################################################################
# # # # From the Django for scientists tutorial modified
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
# from plot.models import InputForm
from . models import InputForm
# from plot.compute import compute, soma, mean
# from plot.compute import *
from . compute import *

## ## Function for the graph.  template = contas
def index_math(request):
    a = None  # initial value of result
    b = None  # initial value of result
    c = None  # initial value of result
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            r = form.r
            s = form.s
            t = form.t
            u = form.u
            a = compute(r)
            b = soma(r,s,t,u)
            c = mean(r,s,t,u)
    else:
        form = InputForm()

    return render_to_response('plot/contas.html',
            {'form': form,
             'b': '%.2f' % b if isinstance(b, float) else '',
             'a': '%.2f' % a if isinstance(a, float) else '',
             'c': '%.2f' % c if isinstance(c, float) else ''
             }, context_instance=RequestContext(request))


##########################################################################
## ## function for the view I created, with txt file. Template = contas_2p
def index_math_2p(request):
    a = None  # initial value of result
    b = None  # initial value of result
    c = None  # initial value of result
    d = None  # initial value of result
#    f = None  # initial value of result
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            # Creating input variables
            r = form.r
            s = form.s
            t = form.t
            u = form.u
            f = form.f  # for filename
            # For the output
            a = compute(r) # for the compute.py script
            b = soma(r,s,t,u)
            c = mean(r,s,t,u)
            d = write_txt(r,s,t,u,f)
            ############################
            ### For txt file directly from views
            # # # out_file_nm = str('outputfile_from_views_index_math_2p.txt')
            # out_file_nm = str( f + '.txt')
            # fh = open(out_file_nm, 'w')
            # fh.write('Testing output file in views (index_math_2p) for program APK, app plot \n\n')
            # fh.write('Input 1:  ')
            # fh.write(str(r) +'\n')
            # fh.write('Input 2:  ')
            # fh.write(str(s) +'\n')
            # fh.write('Input 3:  ')
            # fh.write(str(t) +'\n')
            # fh.write('Input 4:  ')
            # fh.write(str(u) +'\n\n')
            # fh.write('Sum:  ')
            # fh.write(str(b) +'\n')
            # fh.write('Mean:  ')
            # fh.write(str(c) +'\n')
            # fh.write('Sin of input 1:  ')
            # fh.write(str(a) +'\n')
            # fh.close()

    else:
        form = InputForm()
    return render_to_response('plot/contas_2p.html',
            {'form': form,
             'b': '%.2f' % b if isinstance(b, float) else '',
             'a': '%.2f' % a if isinstance(a, float) else '',
             'c': '%.2f' % c if isinstance(c, float) else '',
             'd': d,
             }, context_instance=RequestContext(request))
####################################################################################

## ## Testing to get results in different pages:  template = contas
# def index_math_3p(request):
#     a = None  # initial value of result
#     b = None  # initial value of result
#     c = None  # initial value of result
#     d = None  # initial value of result
#     f = None  # initial value of result
#     if request.method == 'POST':
#         form = InputForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             r = form.r
#             s = form.s
#             t = form.t
#             u = form.u
#             f = form.f  # for filename
#             a = compute(r) # for the compute.py script
#             b = soma(r,s,t,u)
#             c = mean(r,s,t,u)
#             d = write_txt(r,s,t,u,f)
#         else:
#             form = InputForm()
#
#     return render_to_response('plot/contas_2p.html',
#             {'form': form,
#              'b': '%.2f' % b if isinstance(b, float) else '',
#              'a': '%.2f' % a if isinstance(a, float) else '',
#              'c': '%.2f' % c if isinstance(c, float) else '',
#              'd': d,
#              }, context_instance=RequestContext(request))

