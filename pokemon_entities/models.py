from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название покемона")
    photo = models.ImageField(null=True, blank=True, verbose_name="изображение покемона")
    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField(verbose_name="Широта нахождения покемона")
    longetude = models.FloatField(verbose_name="Долгота нахождения покемона")
    appeared_at = models.DateTimeField(null=True, verbose_name="время и дата появления покемона")
    disappeared_at = models.DateTimeField(null=True, verbose_name="время и дата исчезновения покемона")
    level = models.IntegerField(null=True, verbose_name="уровень покемона")
    health = models.IntegerField(null=True, verbose_name="здоровье")
    strength = models.IntegerField(null=True, verbose_name="сила")
    defence = models.IntegerField(null=True, verbose_name="защита")
    stamina = models.IntegerField(null=True, verbose_name="выносливость")


    def __str__(self):
        return self.pokemon.title, self.latitude, self.longetude
