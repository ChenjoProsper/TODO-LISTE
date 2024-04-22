from django.db import models
from django.contrib.auth.models import User

class Tache(models.Model):
    nom = models.CharField(max_length=100)
    finish = models.BooleanField()
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nom