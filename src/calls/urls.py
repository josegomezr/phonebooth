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
        '<int:id>/',
        views.detail.DetailView.as_view(),
        name='detail'
    ),
]
