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
    # Edit client page
    path('edit_client/<int:client_id>', views.edit_client, name='edit_client'),
    # View client page
    path('client/<int:client_id>', views.view_client, name='client')
]