from django.urls import path, include
from . import views

app_name = 'authentication'

urlpatterns = [
    path('profile/', views.profile.detail.DetailView.as_view(), name='profile-show'),
    path('profile/edit/', views.profile.update.UpdateView.as_view(), name='profile-edit'),
    path('login/', views.login.LoginView.as_view(redirect_authenticated_user=True)),
    path('', include('django.contrib.auth.urls')),
]
