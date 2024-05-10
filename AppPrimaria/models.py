from django.db import models

# Create your models here.
class pokemones(models.Model):
    especie_de_pokemon = models.CharField(max_length=100)
    tipo_de_pokemon = models.CharField(max_length=20)

class objetos(models.Model):
    vidasfera = models.CharField(max_length=200)
    banda_focus = models.TextField()
    baya_zidra = models.IntegerField
    id_pokemon = models.ForeignKey(pokemones, on_delete=models.CASCADE)
