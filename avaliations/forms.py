from django.forms import ModelForm
from .models import Avaliation


class CreateForm(ModelForm):
    class Meta:
        model = Avaliation
        fields = ['user_instagram', 'categoria', 'description',
                  'nomeProduto', 'entregaRapida', ]
