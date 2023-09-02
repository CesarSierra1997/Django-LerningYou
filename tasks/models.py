from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Creando modelo para el Crud de tareas


class Task(models.Model):
    title = models.CharField(max_length=100)
    # Por defecto campo basio si no se escribe nada
    description = models.TextField(blank=True)
    # Crea por defecto la fecha en que se creo
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)  # Campo basio inicialmente
    # Por defecto no todas son importantes
    important = models.BooleanField(default=False)
    # Relaciona el FK del User
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title+" - usuario: "+self.user.username
