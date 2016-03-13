# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from contacts.models import Contact
import forms


class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'


from django.core.urlresolvers import reverse
from django.views.generic import CreateView

class CreateContactView(CreateView):
    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')







