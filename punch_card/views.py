from django.shortcuts import render
from .models import Client

def index(request):
    """The home page for punch card"""
    return render(request, 'punch_card/index.html')

def roster(request):
    """A page listing all the clients on the roster"""
    clients = Client.objects.order_by('last_name')
    return render(request, 'punch_card/roster.html', {'clients': clients})