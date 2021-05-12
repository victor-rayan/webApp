from django.test import TestCase
import pytest
from django.urls import reverse, resolve
from mixer.backend.django import mixer

# Create your tests here.

class testUrls:
  def test_avaliation_url(self):
    path = reverse('detail', kwargs={'pk':1})
    assert resolve(path).view_name == 'avaliationDetail'

@pytest.mark.django_db
class testModels:
  avaliation = mixer.blend('avaliations.Avaliation', titleAvaliation= 'Avaliation_test' )
  assert avaliation.__str__ == 'Avaliation_tests'