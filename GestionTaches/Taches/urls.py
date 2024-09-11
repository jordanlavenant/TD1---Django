from django.urls import path
from . import views

urlpatterns = [
  path('', views.task_listing,name="listing"),
]
