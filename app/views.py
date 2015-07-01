from django.shortcuts import render, get_object_or_404,render_to_response
from django.http import HttpResponse
from app.models import Jugador

def index(request):
	jugadores = Jugador.objects.all()
	return HttpResponse("Estamos creando la view")
#	return render_to_response('Jugador/index.html', {'jugadores':jugadores})
	#res_string = "Jugadores <br/>"
	#res_string += '<br/>'.join(["id: %s,"])

# Create your views here.
#def jugador_detalle(request, jugador_id):
#	jugador = get_object_or_404(Jugador, pk=jugador_id)
#	return render_to_response('Jugador/jugador_detalle.html', {'jugador':jugador})

