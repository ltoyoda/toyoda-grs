from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


##################################################################################3
# pip install django-geoposition
# Use  Lat/Lng Object Literals,  e.g. {'lat': 52.5, 'lng': 13.4}.
#from django.db import models

from django.db import models
from geoposition.fields import GeopositionField


class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    # address = models.CharField(max_length=255)
    # city = models.CharField(max_length=50)
    # zipcode = models.CharField(max_length=10)
    position = GeopositionField(blank=True)

    class Meta:
        verbose_name_plural = 'points of interest'