from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()


    def __str__(self):
        return ' '.join([self.first_name, self.last_name])

# # run python manage.py makemigrations contacts
# # python manage.py migrate contacts