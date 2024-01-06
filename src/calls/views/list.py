from django.views.generic.list import ListView as BaseListView
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from ..models import Call


@method_decorator(login_required, name='dispatch')
class ListView(BaseListView):
    model = Call

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs
