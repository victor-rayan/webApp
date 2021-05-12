from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect


def clear_user_instagram(value):
    if value[0] == '@':
        return value
    raise ValidationError("ERRO! Faltou o '@'")
