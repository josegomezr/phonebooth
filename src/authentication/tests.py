import os

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SimpleTest(TestCase):
  def setUp(self):
    User = get_user_model()
    self.dummy_user = User.objects.create_user(
      'testuser',
      'testuser@example.com',
      'testpassword'
    )

  def test_login_unsuccessful(self):
    User = get_user_model()

    response = self.client.post(
      reverse('authentication:login'),
      data={
        'username': 'randomrandom',
        'password': 'randomrandom',
      }
    )

    self.assertEqual(response.status_code, 200)
    self.assertFalse(response.context['form'].is_valid())

  def test_login_fuzzzrandomchars(self):
    User = get_user_model()

    response = self.client.post(
      reverse('authentication:login'),
      data={
        'username': str(os.urandom(32)),
        'password': str(os.urandom(32)),
      }
    )

    self.assertEqual(response.status_code, 200)
    self.assertFalse(response.context['form'].is_valid())


  def test_login_huge_userpass(self):
    User = get_user_model()

    response = self.client.post(
      reverse('authentication:login'),
      data={
        'username': 'A'*256,
        'password': 'A'*256,
      }
    )

    self.assertEqual(response.status_code, 200)
    self.assertFalse(response.context['form'].is_valid())

  def test_login_valid(self):
    User = get_user_model()

    response = self.client.post(
      reverse('authentication:login'),
      data={
        'username': 'testuser',
        'password': 'testpassword',
      },
    )
    self.assertEqual(response.status_code, 302)

  def test_login_valid_matches_user(self):
    User = get_user_model()

    response = self.client.post(
      reverse('authentication:login'),
      data={
        'username': 'testuser',
        'password': 'testpassword',
      },
      follow=True,
    )

    self.assertEqual(response.context['user'], self.dummy_user)
