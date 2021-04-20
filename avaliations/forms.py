from django import forms
from .models import Avaliation, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class CreateForm(forms.ModelForm):
    class Meta:
        model = Avaliation
        fields = ['user_instagram', 'category', 'description',
                  'titleAvaliation', 'deliveryTime', 'ratingAvaliation']
        widgets = {
            'user_instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'titleAvaliation': forms.TextInput(attrs={'class': 'form-control'}),
            'deliveryTime': forms.Select(attrs={'class': 'form-control'}),
            'ratingAvaliation': forms.Select(attrs={'class': 'form-control'}),
        }
