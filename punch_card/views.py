from django.shortcuts import render

def index(request):
    """The home page for punch card"""
    return render(request, 'punch_card/index.html')