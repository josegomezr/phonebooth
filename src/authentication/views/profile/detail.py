from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView

from authentication.models import User


@method_decorator(login_required, name='dispatch')
class DetailView(DetailView):
    model = User

    def get_queryset(self):
        self.kwargs['pk'] = self.request.user.id
        return self.model.objects.all()
