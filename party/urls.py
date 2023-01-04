from django.contrib import admin #不要だが念の為
from django.urls import path
from . import views


app_name = 'party'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create_party/', views.PartyCreateView.as_view(), name='create_party'),
    path('delete_party/<int:pk>', views.PartyDeleteView.as_view(), name='delete_party'),
    path('party_detail/<int:pk>', views.PartyDetailView.as_view(), name='party_detail'),
    path('join_for_party/', views.join_for_party, name='join_for_party'),
    path('not_join_for_party/', views.not_join_for_party, name='not_join_for_party'),
    path('tbd_for_party', views.tbd_for_party, name='tbd_for_party'),
]

