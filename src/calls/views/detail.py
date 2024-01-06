from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView as BaseDetailView

from ..models import Call


@method_decorator(login_required, name='dispatch')
class DetailView(BaseDetailView):
    model = Call

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
