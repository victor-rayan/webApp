from .validate import clear_user_instagram
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from account.models import Account
<<<<<<< HEAD
from ckeditor.fields import RichTextField

=======
from . import validate
# Create your models here.
>>>>>>> passwordChange

# Create your models here.

class Avaliation(models.Model):
<<<<<<< HEAD
    type_RATING = (
        (1, 'star1'),
        (2, 'star2'),
        (3, 'star3'),
        (4, 'star4'),
        (5, 'star5'),
    )

    author = models.ForeignKey(Account , on_delete=models.CASCADE, default=None, null=True)
    store_instagram = models.CharField(
        max_length=25, verbose_name='Instagram Avaliado(Ex:@lojinha)')
    category = models.CharField(max_length=25, default='...')
    description = RichTextField(blank = True, null = True)
=======
    type_CATEGORY = (
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
    )

    author = models.ForeignKey(
        Account, on_delete=models.CASCADE, default=None, null=True)
    store_instagram = models.CharField(
        max_length=25, verbose_name='Instagram Avaliado(Ex:@lojinha)', validators=[clear_user_instagram])
    category = models.CharField(max_length=25, choices=type_CATEGORY,)
    description = models.TextField(verbose_name='Conte sobre o produto')
>>>>>>> passwordChange
    titleAvaliation = models.CharField(
        max_length=100, verbose_name='Titulo do Produto')

    ratingAvaliation = models.IntegerField(
        default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Account, related_name='avaliations')

    def __str__(self):
        return self.titleAvaliation

    def total_likes(self):
        return self.likes.count()
