from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Painting
from inicio.forms import ChargePainting, SearchPainting
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def charge_painting(request):
    painting = None
    if request.method == 'POST':
        form_painting = ChargePainting(request.POST)
        if form_painting.is_valid():
            info = form_painting.cleaned_data

            painting = Painting(artist=info.get('artist'), style=info.get('style'), price=info.get('price'))
            painting.save()

            return redirect('painting_list')
    else:
        form_painting = ChargePainting()
    #print('GET', request.GET)
    #print('POST', request.POST)

    return render(request, 'charge_painting.html', {'saved_painting': painting, 'form_painting': form_painting} )

def painting_list(request):
    search_form = SearchPainting(request.GET)
    if search_form.is_valid():
        artist_to_search = search_form.cleaned_data.get('artist')
        painting_availables = Painting.objects.filter(artist__icontains=artist_to_search)

    return render(request, 'painting_list.html', {'painting_availables': painting_availables, 'search_form': search_form})

def view_painting(request, painting_id):
    painting = Painting.objects.get(id=painting_id)
    return render(request, 'view_painting.html', {'painting': painting})


# Clase basada en vistas
class UpdatePaintingInfo(UpdateView):
    model = Painting
    template_name = 'update_painting_info.html'
    fields = '__all__' # fields = ['Artist, 'Style]: si solo se quieren modificar algunos de lso campos
    success_url = reverse_lazy('painting_list')

class DeletePainting(DeleteView):
    model = Painting
    template_name = 'delete_painting.html'
    success_url = reverse_lazy('painting_list')
