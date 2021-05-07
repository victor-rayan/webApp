import pytest

@pytest.fixture
def user_data():
  return{'email': 'test_email', 'username': 'test_user',
  'instagram': '@test_user', 'state': 'DF', 'birth_date': '27/04/1998'}