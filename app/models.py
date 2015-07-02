from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     followers = models.ManyToManyField('self', related_name='followees', symmetrical=False)


# class Post(models.Model):
#     author = models.ForeignKey(User, related_name='posts')
#     title = models.CharField(max_length=255)
#     body = models.TextField(blank=True, null=True)


# class Photo(models.Model):
#     post = models.ForeignKey(Post, related_name='photos')
#     image = Gmodels.ImageField(upload_to="%Y/%m/%d")

#########Campeonato#######
class Campeonato(models.Model):
    Nombre = models.CharField(max_length=100)

    def __str__(self):
    	return str(self.Nombre)
###########Facultad######
class Facultad(models.Model):
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return  str(self.Nombre)

##########Escuela##########
class Escuela(models.Model):
    Nombre= models.CharField(max_length=50)
    Facultad= models.ForeignKey("Facultad")

    def __str__(self):
        return str(self.Nombre)


###########Genero######
class Genero(models.Model):
	Descripcion = models.CharField(max_length=12)

	def __str__(self):
		return str(self.Descripcion)

###########Semestre#########
class Semestre(models.Model):
    Nivel    = models.CharField(max_length=10)

    def __str__(self):
        return str(self.Nivel)
############Disciplina####
class Disciplina(models.Model):
    Nombre = models.CharField(max_length=50)
    Reglamento = models.TextField(blank=True, null=True)
    Costo = models.CharField(max_length=10)
    Numero_Jugadores = models.CharField(max_length=2)
    Campeonato = models.ForeignKey("Campeonato")

    def __str__(self):
        return str(self.Nombre)


##########Jugador#########
class Jugador(models.Model):
    Apellidos = models.CharField(max_length=50)
    Cedula    = models.CharField(max_length=10)
    Equipo    = models.ForeignKey("Equipo")
    Foto      = models.ImageField(upload_to='PlayerPhotos')
    Nombres   = models.CharField(max_length=50)
    Semestre  = models.ForeignKey("Semestre")
    Telefono  = models.CharField(max_length=50)

#########Equipo#########
class Equipo(models.Model):
    Genero = models.ForeignKey("Genero") 
    Nombre = models.CharField(max_length=50)

    def __str__(self):
    	return str(self.Nombre)

##########Arbitro##############
class Arbitro(models.Model):
    Nombre   = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Nombre)

##############Areas###########
class Areas(models.Model):
    Nombre = models.CharField(max_length=50)
    Lugar  = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Nombre)

###########Disciplina################
#class Inscripciones(models.Model):



    

    #def __unicode__(self):
    #	return "{0} {1}".format(self.Nombres, self.Apellidos)

