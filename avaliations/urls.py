from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.createForm, name="create-form"),
    path('', views.createForm),
]
