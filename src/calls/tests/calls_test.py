import os

from django.contrib.auth import get_user_model, REDIRECT_FIELD_NAME
from django.test import TestCase
from django.urls import reverse

from ..models import Call

class SimpleTest(TestCase):
  def _auth_redirect_url_to(self, to):
    return '{}?{}={}'.format(
        reverse('authentication:login'),
        REDIRECT_FIELD_NAME,
        to,
      )

  def setUp(self):
    User = get_user_model()
    self.da_user = User.objects.create_user(
      'testuser',
      'testuser@example.com',
      'testpassword'
    )

  def test_calls_need_authentication(self):
    response = self.client.get(
      reverse('calls:list')
    )

    self.assertRedirects(response,
      self._auth_redirect_url_to(reverse('calls:list'))
    )

  def test_calls_empty(self):
    self.client.force_login(self.da_user)

    response = self.client.get(
      reverse('calls:list')
    )

    self.assertContains(response, 'No calls yet')

  def test_call_list(self):
    self.client.force_login(self.da_user)

    response = self.client.get(
      reverse('calls:list')
    )

    self.skipTest("TODO: Pending test")
    self.assertNotContains(response, 'No calls yet')

  def test_call_detail(self):
    self.client.force_login(self.da_user)

    return self.skipTest("TODO: Pending test")

    response = self.client.get(
      reverse('calls:detail', pk=call.id)
    )

    self.assertContains(call.id, 'No calls yet')

  def test_call_detail_404(self):
    self.client.force_login(self.da_user)

    response = self.client.get(
      reverse('calls:detail', kwargs={'pk':'99999999999999'})
    )

    self.assertEqual(
      response.status_code,
      404
    )

  def test_call_detail_bad_id(self):
    self.client.force_login(self.da_user)

    url = reverse('calls:detail', kwargs={'pk':'99123499'})
    # force a random value in the uri param
    url.replace('/99123499/', 'AAA')

    response = self.client.get(url)

    self.assertEqual(
      response.status_code,
      404
    )

