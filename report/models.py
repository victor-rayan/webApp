from django.db import models
from django.contrib.auth import get_user_model
from account.models import Account
from .validate import clear_user_instagram
# Create your models here.


class Report(models.Model):
    store_instagram_report = models.CharField(
        max_length=100, verbose_name='Loja denunciada', validators=[clear_user_instagram])
    titleReport = models.CharField(
        max_length=100, verbose_name='Titulo da denúncia:')
    descriptionReport = models.TextField(
        verbose_name='Nos conte o que aconteceu:')

    def __str__(self):
        return self.titleReport
