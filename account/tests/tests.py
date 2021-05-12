from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.False

class UserAccountTests(TestCase):

  def test_new_superuser(self):
    db = get_user_model()
    super_user = db.object.create_superuser(
      'testuser@super.com', 'username', 'password'
    )
    self.assertEqual(super_user.email, 'testuser@super.com')
    self.assertEqual(super_user.username, 'username')
    self.assertTrue(super_user.is_superuser)
    self.assertTrue(super_user.is_staff)
    self.assertTrue(super_user.is_active)
    self.assertEqual(str(super_user), "username")

  def test_new_user(self):
    db = get_user_model()
    user = db.object.create_user(
      'test@newuser.com', 'username1', 'password'
    )
    self.assertEqual(user.email, 'test@newuser.com')
    self.assertEqual(user.username, 'username1')

    with self.assertRaises(ValueError):
      db.object.create_user(
        '', 'username2', 'password'
      )
    with self.assertRaises(ValueError):
      db.object.create_user(
        'test2@newuser.com', '', 'password'
      )