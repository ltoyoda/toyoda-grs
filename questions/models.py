from django.db import models
from django.forms import ModelForm
from math import pi

class Input(models.Model):
    # Initial questions
    file = models.CharField(
        verbose_name=' Please give a name to your file (e.g. Rapport Company 3) ', max_length=200,  default='Railway Rapport')
    q1 = models.FloatField(
        verbose_name=' Date', default=1 )
    q2 = models.CharField(
        verbose_name=' Are there any visible signs of the deformation? ', max_length=200, default='Yes')
    q3 = models.CharField(
        verbose_name=' If so can is it subsidence or uplift?', max_length=200, default='Choose')
    q4 = models.CharField(
        verbose_name=' When did you first noticed it? (month/year)', max_length=200, default='January 2002')
    q5 = models.CharField(
        verbose_name=' Deformation pattern in time', max_length=200, default='00')
    q6 = models.CharField(
        verbose_name=' Another question', max_length=200, default='00')

    # Semi-Variogram questions for the graph
    defo = models.FloatField(
        verbose_name=' What is the maximum deformation expected at the centre of the Area of interest (mm)? ', default=0.2)
    a = models.FloatField(
        verbose_name=' Correlation at distance 100 (m)', default=1)
    b = models.FloatField(
        verbose_name=' Correlation at distance 500 (m)', default=1)
    c = models.FloatField(
        verbose_name='  Correlation at distance 1000 (m)', default=1)
    d = models.FloatField(
        verbose_name='  Correlation at distance 5000 (m)', default=0.5)
    e = models.FloatField(
        verbose_name='  Correlation at distance 10000 (m)', default=0.25)
    f = models.FloatField(
        verbose_name='Correlation at distance 15000 (m)', default=0.1)
    g = models.FloatField(
        verbose_name='Correlation at distance 20000 (m)', default=0)
    h = models.FloatField(
        verbose_name='Correlation at distance 25000 (m)', default=0.0)
    i = models.FloatField(
        verbose_name='Correlation at distance 30000 (m)', default=0.0)


class InputForm(ModelForm):
    class Meta:
        model = Input
        # This part determines the order of the questions
        fields = ['file','defo', 'a', 'b', 'c', 'd', 'e','f','g','h','i']
        # fields = ['file','q1','q2','q3','q4','q5','q6','defo', 'a', 'b', 'c', 'd', 'e','f','g','h','i']
        questions = ['q1','q2','q3','q4','q5','q6']