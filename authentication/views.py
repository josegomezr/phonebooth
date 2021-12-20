from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .forms import AuthenticationForm


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'authentication/profile.html'


class LoginView(BaseLoginView):
    authentication_form = AuthenticationForm
