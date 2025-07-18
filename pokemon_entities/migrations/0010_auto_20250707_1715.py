# Generated by Django 2.2.24 on 2025-07-07 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_pokemon_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='parent',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon', verbose_name='Предыдущая эволюция'),
        ),
    ]
