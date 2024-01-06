from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.utils.translation import gettext_lazy as _

from phonebooth.utils import BootstrapifyFormMixin

class LoginView(SuccessMessageMixin, BootstrapifyFormMixin, BaseLoginView):
    def get_success_message(self, cleaned_data):
        return _('Welcome %(full_name)s.' % {
            'full_name' : self.request.user.full_name
        })
