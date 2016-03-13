from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from hw1.models import InputForm
from hw1.compute import compute
import os

def index(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute( form2.a, form2.b, form2.c, form2.d, form2.e, form2.f, form2.g, form2.h, form2.i, form2.file)
            result = result.replace('static/', '')
    else:
        form = InputForm()

    return render_to_response('hw1/vib1.html',
            {'form': form,
             'result': result,
             'title':'Spatial variation',
             'message':'Questions - Variogram ',
             'content': 'This is the text of the main page, here we can write whatever we want!!!....',

             }, context_instance=RequestContext(request))

##########################################################################################
def index_math_2p(request):
    # a = None  # initial value of result
    # b = None  # initial value of result
    # c = None  # initial value of result
    # d = None  # initial value of result
    result = None  # initial value of result
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            # Creating input variables
            q = form.q
            r = form.r
            s = form.s
            t = form.t
            u = form.u
            v = form.v
            x = form.x
            y = form.y
            z = form.z
            f = form.f  # for filename
            # For the output
            # a = compute(r) # for the compute.py script
            # c = mean(r,s,t,u)
            # b = soma(r,s,t,u)
            # d = write_txt(r,s,t,u,f)
            result = compute(q,r,s,t,u,v,x,y,z,f)
            result = result.replace('static/', '')

    else:
        form = InputForm()

    # return render_to_response('plot/contas_2p.html',
    #         {'form': form,
    #          'result': result,
    #          # 'b': '%.2f' % b if isinstance(b, float) else '',
    #          # 'a': '%.2f' % a if isinstance(a, float) else '',
    #          # 'c': '%.2f' % c if isinstance(c, float) else '',
    #          # 'd': d,
    #          'title':'Plotting in two pages!',
    #          'message':'Your application description page (index-index)- change in app/views.py',
    #          'content': 'This is the text of the main page, here we can write whatever we want!!!....',
    #          } , context_instance=RequestContext(request))

    return httpResponse (result)