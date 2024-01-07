from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import BaseDetailView
from django.http.response import HttpResponse
from django.http import Http404

from ...models import Call

from twilio.twiml.voice_response import VoiceResponse


@method_decorator(login_required, name='dispatch')
class VoiceXMLView(BaseDetailView):
    model = Call

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404: # custom 404 handler
            return HttpResponse('404 not found generated in controller', status=404)

    def render_to_response(self, context):
        r = VoiceResponse()
        r.say("Welcome to twilio!")
        return HttpResponse(str(r), content_type='text/xml')
