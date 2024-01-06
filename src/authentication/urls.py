from django.urls import path, include
from .views import EditProfileView, ProfileView, LoginView

app_name = 'authentication'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile-show'),
    path('profile/edit/', EditProfileView.as_view(), name='profile-edit'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True)),
    path('', include('django.contrib.auth.urls')),
]
