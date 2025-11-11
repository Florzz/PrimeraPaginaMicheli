from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Painting

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def charge_painting(request, artist, style, price):
    painting = Painting(artist=artist, style=style, price=price)
    painting.save()
    return render(request, 'charge_painting.html', {'saved_painting': painting} )

def painting_list(request):
    painting = Painting.objects.all
    return render(request, 'painting_list.html', {'painting_availables': painting})