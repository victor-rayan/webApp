from django import forms
from .models import Avaliation
from django.core.validators import validate_slug, validate_email
from django.core.validators import validate_slug, validate_email
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect


class CreateForm(forms.ModelForm):
    class Meta:
        model = Avaliation
        fields = ['user_instagram', 'category', 'description',
                  'titleAvaliation', 'deliveryTime', 'ratingAvaliation']
        widgets = {
            'user_instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'titleAvaliation': forms.TextInput(attrs={'class': 'form-control'}),
            'deliveryTime': forms.Select(attrs={'class': 'form-control'}),
            'ratingAvaliation': forms.Select(attrs={'class': 'form-control'}),
        }
