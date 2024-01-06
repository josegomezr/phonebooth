from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

app_name = 'phonebooth'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls', namespace='authentication')),
    path('', lambda request: redirect('auth/login/', permanent=True)),
]
