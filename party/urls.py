from django.contrib import admin #不要だが念の為
from django.urls import path
from . import views


app_name = 'party'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create_party/', views.PartyCreateView.as_view(), name='create_party'),
]
