from django.urls import path, include
from . import views

app_name = 'calls'

urlpatterns = [
    path(
        '',
        views.list.ListView.as_view(),
        name='list'
    ),
    path(
        '<int:pk>/',
        views.detail.DetailView.as_view(),
        name='detail'
    ),
    path(
        '<int:pk>/twilio/voice-xml',
        views.twilio.voice_xml.VoiceXMLView.as_view(),
        name='twilio_voice-xml'
    ),
]
