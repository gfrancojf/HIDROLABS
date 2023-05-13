from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Muestra

class MuestraDetailView(View):
    def get(self, request, muestra_id):
        muestra = get_object_or_404(Muestra, id=muestra_id)
        return render(request, 'laboratorio/muestra_detalle.html', {'muestra': muestra})
