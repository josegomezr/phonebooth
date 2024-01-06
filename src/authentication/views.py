from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from phonebooth.utils import BootstrapifyFormMixin

from .models import User

@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = User

    def get_queryset(self):
        self.kwargs['pk'] = self.request.user.id
        return self.model.objects.all()


@method_decorator(login_required, name='dispatch')
class EditProfileView(SuccessMessageMixin, BootstrapifyFormMixin, UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email')

    def get_queryset(self):
        self.kwargs['pk'] = self.request.user.id
        return self.model.objects.all()

    def get_success_url(self):
        return reverse('authentication:profile-show')

    def get_success_message(self, cleaned_data):
        return _('Changes saved successfuly!')

class LoginView(SuccessMessageMixin, BootstrapifyFormMixin, BaseLoginView):
    def get_success_message(self, cleaned_data):
        return _('Welcome %(full_name)s.' % {'full_name' : self.request.user.full_name })
