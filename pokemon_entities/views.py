import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.utils.timezone import localtime


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    # with open('pokemon_entities/pokemons.json', encoding='utf-8') as database:
    #     pokemons = json.load(database)['pokemons']
    pokemon_entities = PokemonEntity.objects.filter(appeared_at__lt=localtime(), disappeared_at__gt=localtime())
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longetude,
            request.build_absolute_uri(pokemon_entity.pokemon.photo.url)
        )
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.photo.url),
            'title_ru': pokemon.title,
        })


    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon_requested = Pokemon.objects.get(id=pokemon_id)
    pokemon = {
        "title_ru": pokemon_requested.title,
        "img_url": request.build_absolute_uri(pokemon_requested.photo.url),
        "description": pokemon_requested.description,
        "title_en": pokemon_requested.title_eng,
        "title_jp": pokemon_requested.title_jp,
    }
    previous_evolution = pokemon_requested.previous_evolution
    if previous_evolution:
        pokemon["previous_evolution"] = {
            "pokemon_id": previous_evolution.id,
            "img_url": request.build_absolute_uri(previous_evolution.photo.url),
            "title_ru": previous_evolution.title,
        }
    next_evolution = pokemon_requested.next_evolutions.first()
    if next_evolution:
        pokemon["next_evolution"] = {
            "pokemon_id": next_evolution.id,
            "img_url": request.build_absolute_uri(next_evolution.photo.url),
            "title_ru": next_evolution.title,
        }

    pokemon_entities = PokemonEntity.objects.filter(pokemon=pokemon_requested, appeared_at__lt=localtime(), disappeared_at__gt=localtime())

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longetude,
            request.build_absolute_uri(pokemon_entity.pokemon.photo.url)
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
