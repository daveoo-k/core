from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Szafka(models.Model):
    nazwa       = models.CharField (max_length=300)
    szerokosc   = models.IntegerField(default=False)
    wysokosc    = models.IntegerField(default=False)
    glebokosc   = models.IntegerField(default=False)
    plyta       = models.IntegerField(default=False)