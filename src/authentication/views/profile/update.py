from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from phonebooth.utils import BootstrapifyFormMixin

from authentication.models import User

@method_decorator(login_required, name='dispatch')
class UpdateView(SuccessMessageMixin, BootstrapifyFormMixin, UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email')

    def get_queryset(self):
        self.kwargs['pk'] = self.request.user.id
        return self.model.objects.all()

    def get_success_url(self):
        return reverse('authentication:profile-show')

    def get_success_message(self, cleaned_data):
        return _('Changes saved successfuly!')
