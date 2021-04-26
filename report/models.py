from django.db import models
from django.contrib.auth import get_user_model
from account.models import Account
# Create your models here.


class Report(models.Model):
    titleReport = models.CharField(
        max_length=100, verbose_name='Titulo da denúncia:')
    descriptionReport = models.TextField(
        verbose_name='Nos conte o que aconteceu:')

    def __str__(self):
        return self.titleReport
