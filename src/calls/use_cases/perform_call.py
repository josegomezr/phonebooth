from dataclasses import dataclass

from django.urls import reverse

from ..twilio_client_factory import TwilioClientFactory
from phonebooth.use_cases import UseCase

class PerformCall(UseCase):
    def __init__(self, twilio_client=None):
        self.twilio_client = twilio_client or TwilioClientFactory.for_app()

    @dataclass
    class Request(UseCase.Request):
        to: str
        callback_url: str

        def validate(self):
            if not self.to:
                raise TypeError('Missing "to" field')
            if not self.callback_url:
                raise TypeError('Missing "callback_url" field')

    @dataclass
    class Response(UseCase.Response):
        call_sid: str

    def execute(self, request):
        client = self.twilio_client
        call = client.calls.create(
            to=request.to,
            from_=TwilioClientFactory.app_default_from, # todo: fetch this better
            url=request.callback_url
        )

        # call = client.calls.create(
        #     method='GET',
        #     status_callback=reverse('calls:twilio:voice-callback', dict(call_id='call-id')),
        #     status_callback_method='POST',
        #     url=reverse('calls:twilio:voice-twiml', dict(call_id='call-id')),
        #     to=request.to,
        #     from_=request.from_
        # )        
        # print(call.sid)

        return type(self).Response(call_sid=call.sid)
