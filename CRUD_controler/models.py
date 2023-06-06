
from django.db import models



# Create your models here.
class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 35)
    last_name = models.CharField(max_length = 35)
    nickname = models.CharField(unique=True,max_length=30)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    hora_creacion = models.DateTimeField(auto_now=True)
    pass

class Proyectos(models.Model):
    id_project = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    name_project = models.CharField(unique=True,max_length=100)
    descripcion = models.TextField()
    hora_creacion = models.DateTimeField(auto_now=True)
    pass

class Capitulos(models.Model):
    id_capitulo = models.AutoField(primary_key=True)
    id_project = models.ForeignKey(Proyectos,on_delete=models.CASCADE)
    id_user = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    numero_del_capitulo = models.CharField(max_length=10)
    lista_etiqueta_capitulo = models.CharField(max_length=100)
    contenido_capitulo = models.TextField(max_length= 8000)
    url_capitulo = models.CharField(max_length=400)

    pass

