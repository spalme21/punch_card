from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm

def index(request):
    """The home page for punch card"""
    return render(request, 'punch_card/index.html')

def roster(request):
    """A page listing all the clients on the roster"""
    clients = Client.objects.order_by('last_name')
    return render(request, 'punch_card/roster.html', {'clients': clients})

def new_client(request):
    """Add a new client"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ClientForm()
    else:
        # POST data submitted; process data.
        form = ClientForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('punch_card:roster')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'punch_card/new_client.html', context)