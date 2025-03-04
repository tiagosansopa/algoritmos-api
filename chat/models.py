from django.db import models

class Message(models.Model):
    usuario = models.CharField(max_length=255)
    puntos = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.puntos}"