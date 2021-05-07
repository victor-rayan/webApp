from django import urls
from django.contrib.auth import get_user_model
import pytest

@pytest.mark.django_db
def test_user_signup(client, user_data):
  user_model = get_user_model()
  assert user_model.object.count() == 0
  signup_url = urls.reverse('register')
  resp = client.post(signup_url, user_data)
  assert resp.status_code == 200