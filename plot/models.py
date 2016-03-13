from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


#####################################################################################################
# # # From the Django for scientists tutorial
# This works as forms.py
from django.forms import ModelForm
# from math import pi

class Input(models.Model):
    r = models.FloatField(
        verbose_name=' amplitude (m)', default=1.0)
    s = models.FloatField(
        verbose_name=' damping coefficient (kg/s)', default=2.0)
    t = models.FloatField(
        verbose_name=' frequency (1/s)', default=2*3.141516)
    u = models.FloatField(
        verbose_name=' time interval (s)', default=18)
    f = models.CharField(
        verbose_name=' txt filename ', max_length=200, default = 'out-views_2p')

class InputForm(ModelForm):
    class Meta:
        model = Input
#         fields = ['A', 'b', 'w', 'T']
        fields = ['r', 's', 't', 'u','f']