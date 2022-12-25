from django.contrib import admin #不要だが念の為
from django.urls import path
from . import views


app_name = 'party'

urlpatterns = [
    path('', views.index_view, name='index'), #関数ベース
]
