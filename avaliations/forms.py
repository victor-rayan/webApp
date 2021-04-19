from django import forms
from .models import Avaliation


class CreateForm(forms.ModelForm):
    class Meta:
        model = Avaliation
        fields = ['user_instagram', 'category', 'description',
                  'titleAvaliation', 'deliveryTime', 'rating']
        widgets = {
            'user_instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'titleAvaliation': forms.TextInput(attrs={'class': 'form-control'}),
            'deliveryTime': forms.Select(attrs={'class': 'form-control'}),
            
        }
