from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.shortcuts import redirect, render
from django.views.defaults import page_not_found
from django.conf.urls.static import static

app_name = 'phonebooth'
urlpatterns = []

if settings.ENVIRONMENT != 'production':
    urlpatterns.append(
        path(
            '404/',
            lambda request: page_not_found(request, None)
        )
    )

urlpatterns += [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'auth/',
        include('authentication.urls', namespace='authentication')
    ),
    path(
        'calls/',
        include('calls.urls', namespace='calls')
    ),
    path(
        '',
        lambda request: redirect('auth/login/', permanent=True)
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

