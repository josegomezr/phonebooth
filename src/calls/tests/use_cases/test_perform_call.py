import os

from django.test import TestCase
from phonebooth.use_cases import UseCase
from calls.use_cases.perform_call import PerformCall

class PerformCallTest(TestCase):
  def test_request_with_none(self):
    with self.assertRaises(TypeError):
      PerformCall.Request(to=None)

  def test_request_no_args(self):
    with self.assertRaises(TypeError):
      PerformCall.Request()

  def test_performs_call(self):
    req = PerformCall.Request(to='+12345667')
    use_case = PerformCall()
    use_case(req)

