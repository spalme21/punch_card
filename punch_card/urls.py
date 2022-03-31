"""Defines URL patterns for punch_card"""

from django.urls import path
from . import views

app_name = 'punch_card'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Roster page
    path('roster/', views.roster, name='roster'),
    # New client page
    path('new_client/', views.new_client, name='new_client'),
]