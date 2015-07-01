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
#     image = models.ImageField(upload_to="%Y/%m/%d")
class Campeonato(models.Model):
    Nombre = models.CharField(max_length=100)

  #  def __unicode__(self):
   # 	return str(self.Nombre)

class Equipo(models.Model):
    Nombre = models.CharField(max_length=50)
    Genero = models.CharField(max_length=10)

    def __str__(self):
    	return str(self.Nombre)

class Jugador(models.Model):
    Cedula    = models.CharField(max_length=10)
    Apellidos = models.CharField(max_length=50)
    Nombres   = models.CharField(max_length=50)
    Semestre  = models.CharField(max_length=50)
    Telefono  = models.CharField(max_length=50)
    Equipo = models.ForeignKey("Equipo")


    #def __unicode__(self):
    #	return "{0} {1}".format(self.Nombres, self.Apellidos)

