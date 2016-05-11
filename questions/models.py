from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from math import pi


class Project(models.Model):
    ''' Creating input fields for the whole web interface '''

    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    direction = models.CharField(max_length=200)
    defo_type = models.CharField(max_length=200)
    defo_depth = models.CharField(max_length=200)
    defo_start_date = models.DateTimeField()
    defo_model = models.DateTimeField()
    visible_signs = models.DateTimeField()
    major_event = models.CharField(max_length=200)


class CoordAOI(models.Model):
    '''Point Coordinates or Area of Interest'''
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    lon = models.DecimalField(max_digits=8, decimal_places=3)
    input = models.ForeignKey(Project)

    def __str__(self):
        return (self.lat, self.lon)


class SquareAOI(models.Model):
    '''Square Coordinates or Area of Interest'''
    lat_first = models.DecimalField(max_digits=8, decimal_places=3)
    lon_first = models.DecimalField(max_digits=8, decimal_places=3)
    lat_second = models.DecimalField(max_digits=8, decimal_places=3)
    lon_second = models.DecimalField(max_digits=8, decimal_places=3)
    input = models.ForeignKey(Project)

    def __str__(self):
        return [(self.lat_first, self.lon_first),(self.lat_second, self.lon_second)]


class CoordStable(models.Model):
    ''' Coordinates Stable Point '''
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    lon = models.DecimalField(max_digits=8, decimal_places=3)
    input = models.ForeignKey(Project)

    def __str__(self):
        return (self.lat, self.lon)


class CoordConstruction(models.Model):
    '''Coordinates Major Construction Area '''
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    lon = models.DecimalField(max_digits=8, decimal_places=3)
    input = models.ForeignKey(Project)

    def __str__(self):
        return (self.lat, self.lon)


class CorrelationDistance(models.Model):
    ''' Input values for the Variogram and map visualization '''
    distance = models.FloatField()
    percentage = models.FloatField()
    input = models.ForeignKey(Project)

    def __str__(self):
        return ' Correlation at distance {} (m)'.format(self.distance)

