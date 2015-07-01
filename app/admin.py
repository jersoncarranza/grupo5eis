from django.contrib import admin
from app.models import Campeonato,Equipo, Jugador #,  Jugador , Facultad, Disciplina, Escuela # , Arbitro, Area, Evento 


class EquipoInline(admin.StackedInline):
	model = Equipo
	extra = 2

class JugadorAdmin(admin.ModelAdmin):
	list_display = ('Apellidos','Nombres','Semestre')
	list_filter = ['Equipo','Semestre']
	#pass
	#inlines = [JugadorInline]


class EquipoAdmin(admin.ModelAdmin):
	pass
	#inlines = [EquipoInline]



admin.site.register(Campeonato)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
#admin.site.register(Facultad)
#admin.site.register(Disciplina)
#admin.site.register(Escuela)
#admin.site.register(Evento)
#admin.site.register(Arbitro)
#admin.site.register(Area)


# Register your models here.
