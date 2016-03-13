from django.db import models
from django.forms import ModelForm
from math import pi

class Input(models.Model):
    defo = models.FloatField(
        verbose_name=' What is the maximum deformation expected at the centre of the event (mm)', default=0.2)
    a = models.FloatField(
        verbose_name=' Correlation at distance 100 (m)', default=1)
    b = models.FloatField(
        verbose_name=' Correlation at distance 500 (m)', default=1)
    c = models.FloatField(
        verbose_name='Correlation at distance 1000 (m)', default=1)
    d = models.FloatField(
        verbose_name='Correlation at distance 5000 (m)', default=0.5)
    e = models.FloatField(
        verbose_name='Correlation at distance 10000 (m)', default=0.25)
    f = models.FloatField(
        verbose_name='Correlation at distance 15000 (m)', default=0.1)
    g = models.FloatField(
        verbose_name='Correlation at distance 20000 (m)', default=0)
    h = models.FloatField(
        verbose_name='Correlation at distance 25000 (m)', default=0.0)
    i = models.FloatField(
        verbose_name='Correlation at distance 30000 (m)', default=0.0)
    file = models.CharField(
        verbose_name=' file name ', max_length=200,  default='first graph')

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ['defo', 'a', 'b', 'c', 'd', 'e','f','g','h','i','file',]
