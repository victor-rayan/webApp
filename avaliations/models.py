from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
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

    author = models.ForeignKey(Account , on_delete=models.CASCADE, default=None, null=True)
    store_instagram = models.CharField(
        max_length=25, verbose_name='Instagram Avaliado(Ex:@lojinha)')
    category = models.CharField(max_length=25, default='...')
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
        return self.titleAvaliation

    def total_likes(self):
        return self.likes.count()
