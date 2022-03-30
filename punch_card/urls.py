"""Defines URL patterns for punch_card"""

from django.urls import path
from . import views

app_name = 'punch_card'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]