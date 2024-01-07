from django.test import TestCase
from phonebooth.use_cases import UseCase

class UseCaseTest(TestCase):
  def test_accepts_only_request_type(self):
    use_case = UseCase()
    with self.assertRaises(TypeError):
      use_case(None)

  def test_accepts_with_request_type(self):
    use_case = UseCase()
    with self.assertRaises(NotImplementedError):
      use_case(UseCase.Request())
