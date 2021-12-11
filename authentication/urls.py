from django.urls import path, include
from .views import ProfileView

app_name = 'authentication'

urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('', include('django.contrib.auth.urls')),
]
