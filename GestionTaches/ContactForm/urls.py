from django.urls import path
from . import views

urlpatterns=[
    path('', views.contacts, name='contacts'),
    path('add', views.ContactForm.contact, name='create_contact'),
    path('<cid>', views.contact, name='contact'),
    path('<cid>/delete', views.delete, name='delete_contact'),
    path('<cid>/edit', views.edit, name='edit_contact'),
]