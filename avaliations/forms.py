from django import forms
from .models import Avaliation


class CreateForm(forms.ModelForm):
    class Meta:
        model = Avaliation
        fields = ['user_instagram', 'categoria', 'description',
                  'nomeProduto', 'entregaRapida', ]
        widgets = {
            'user_instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'nomeProduto': forms.TextInput(attrs={'class': 'form-control'}),
            'entregaRapida': forms.Select(attrs={'class': 'form-control'}),
        }
