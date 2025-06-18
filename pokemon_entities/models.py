from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название покемона")
    photo = models.ImageField(null=True, blank=True, verbose_name="изображение покемона")

    def __str__(self):
        return self.title
