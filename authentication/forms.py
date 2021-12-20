from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from django.core import validators
from django.forms.utils import ErrorDict, ErrorList
from phonebooth.utils import BootstrapifyMixin

from .models import User


class AuthenticationForm(BootstrapifyMixin, BaseAuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].validators.append(validators.MinLengthValidator(5))
        self.fields['username'].widget.attrs['minlength'] = 5

        self.fields['password'].validators.append(validators.MinLengthValidator(6))
        self.fields['password'].widget.attrs['minlength'] = 5
