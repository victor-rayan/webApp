from django.db import models
from django.contrib.auth import get_user_model
from account.models import Account

# Create your models here.


class Avaliation(models.Model):
    type_RATING = (
        (1, 'star1'),
        (2, 'star2'),
        (3, 'star3'),
        (4, 'star4'),
        (5, 'star5'),
    )
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

    user_instagram = models.CharField(
        max_length=25, verbose_name='Instagram Avaliado(Ex:@lojinha)')
    category = models.CharField(max_length=25, choices=type_CATEGORY,)
    description = models.TextField(verbose_name='Conte sobre o produto')
    titleAvaliation = models.CharField(
        max_length=100, verbose_name='Titulo do Produto')

    deliveryTime = models.IntegerField(
        choices=type_RATING, verbose_name='Velocidade da Entrega'
    )

    ratingAvaliation = models.IntegerField(
        choices=type_RATING, verbose_name='Nota de Avaliação')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Account, related_name='avaliations')

    def __str__(self):
        return self.user_instagram

    def total_likes(self):
        return self.likes.count()
