from django.urls import path, include
from . import views

urlpatterns = [
    path('criar/', views.createForm, name="create-form"),
    path('', views.createForm),
]
