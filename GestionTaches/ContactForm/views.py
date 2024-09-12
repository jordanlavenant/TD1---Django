from django.shortcuts import get_object_or_404, render, redirect
from django.forms import ModelForm, Textarea
from .models import Contact
from django import forms
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages


def contacts(request):
  contacts = Contact.objects.all()
  context = {'contacts': contacts}
  return render(request,'contacts.html', context)

class ContactForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    self.fields['name'].label = "Nom "
    self.fields['firstname'].label = "Prenom"
    self.fields['email'].label = "mél"

  class Meta:
    model = Contact
    fields = ('name', 'firstname', 'email', 'message')
    widgets = {'message': Textarea(attrs={'cols': 60, 'rows': 10})}

  def contact(request):
    form = ContactForm()
    if request.method == "POST":
      form = ContactForm(request.POST)
      if form.is_valid():
        new_contact = form.save()
        messages.success(request, 'Nouveau contact ' + new_contact.name + ' ' + new_contact.email)
        return redirect(reverse('contact', args=[new_contact.pk]))
    context = {'form': form}
    return render(request, 'add_contact.html', context)

def contact(request, cid):
  contact = get_object_or_404(Contact, pk=cid)
  context = {'pers': contact}
  return render(request,'contact.html', context)

def delete(request, cid):
  contact = get_object_or_404(Contact, pk=cid)
  contact.delete()
  return redirect('contacts')

class ContactEditForm(ModelForm):
  class Meta:
    model = Contact
    fields = ('name', 'firstname', 'email', 'message')
    widgets = {'message': Textarea(attrs={'cols': 60, 'rows': 10})}

def edit(request, cid):
  contact = get_object_or_404(Contact, pk=cid)
  if request.method == "POST":
    form = ContactEditForm(request.POST, instance=contact)
    if form.is_valid():
      form.save()
      messages.success(request, 'Contact mis à jour avec succès')
      return redirect(reverse('contact', args=[contact.pk]))
  else:
    form = ContactEditForm(instance=contact)
  context = {'form': form, 'contact': contact}
  return render(request, 'edit_contact.html', context)