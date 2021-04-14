from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.createForm, name="create-form"),
    path('', views.createForm),
    path('update/<str:pk>/', views.updateForm, name="update-form"),
    path('delete/<str:pk>/', views.deleteForm, name="delete-form"),
]
