from django.db import models

class Supervisor (models.Model):
    idSupervisor = models.IntegerField()
    nombreSupervisor = models.CharField(max(80))