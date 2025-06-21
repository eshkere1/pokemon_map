from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название покемона")
    photo = models.ImageField(null=True, blank=True, verbose_name="изображение покемона")

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField(verbose_name="Широта нахождения покемона")
    longetude = models.FloatField(verbose_name="Долгота нахождения покемона")
    appeared_at = models.DateTimeField(verbose_name="время и дата появления покемона")
    disappeared_at = models.DateTimeField(verbose_name="время и дата исчезновения покемона")

    def __str__(self):
        return self.title
