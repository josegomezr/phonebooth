from django.conf import settings
from twilio.rest import Client

class TwilioClientFactory:
    @staticmethod
    def app_default_from():
        return settings.TWILIO_FROM_NUMBER

    @staticmethod
    def for_app():
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.api.base_url = 'http://127.0.0.1:4010/' # TODO: parametrize for devel & test.
        return client
