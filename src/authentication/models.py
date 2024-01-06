from django.utils.functional import cached_property
from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    @cached_property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
