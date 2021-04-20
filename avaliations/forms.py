from django import forms
from .models import Avaliation

choice_list = [
    ('autos_e_pecas', 'Autos e Peças'),
    ('para_sua_casa', 'Para a Sua Casa'),
    ('eletronicos_e_celulares', 'Eletrônicos e celulares'),
    ('musica_e_hobbies', 'Musicas e Hobbies'),
    ('artigos_infatis', 'Artigos Infantis'),
    ('moda_e_beleza', 'Moda e Beleza'),
    ('animais_de_estimacao', 'Animais de Estimação'),
    ('servicos', 'Serviços'),
    ('agro_e_industrias', 'Agro e Industrias'),
    ('esportes_e_lazer', 'Esportes e Lazer'),
    ('comercio_e_escritorio', 'Comercio e Escritorio'),
]


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
