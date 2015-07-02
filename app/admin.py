from django.contrib import admin
from app.models import Campeonato, Genero ,Equipo, Jugador, Semestre ,Facultad, Escuela, Disciplina, Arbitro, Areas
class GeneroAdmin(admin.ModelAdmin):
	pass

class EquipoInline(admin.StackedInline):
	model = Equipo
	extra = 2

class JugadorAdmin(admin.ModelAdmin):
	list_display = ('Apellidos','Nombres','Semestre','Foto')
	list_filter = ['Equipo','Semestre']
	#pass
	#inlines = [JugadorInline]


class EquipoAdmin(admin.ModelAdmin):
	list_filter = ['Genero']
	#inlines = [EquipoInline]



admin.site.register(Facultad)
admin.site.register(Disciplina)
admin.site.register(Escuela)
admin.site.register(Campeonato)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Semestre)
admin.site.register(Arbitro)
admin.site.register(Areas)

#admin.site.register(Evento)
#admin.site.register(Arbitro)
#admin.site.register(Area)


# Register your models here.
