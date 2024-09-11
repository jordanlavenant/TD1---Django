from django.shortcuts import render
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
  class Meta:
    model = Contact
    fields = ('name', 'firstname', 'email', 'message')

  def contact(request):
    contact_form = ContactForm()
    return render(request,'contact.html', {'contact_form' : contact_form})