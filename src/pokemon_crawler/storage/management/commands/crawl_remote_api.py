import requests
from django.core.management.base import BaseCommand

from pokemon_crawler.storage.models import Ability, Form, Move, Pokemon, Stat, Type


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        offset = 0
        limit = 20
        response = True

        url = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20"

        while response:
            info = requests.get(url)
            content = info.json()

            if info.status_code != 200:
                response = False

            url = content['next']
            offset += limit

            print(f"current offset {offset}")

            self.add_pokemon(content['results'])

    def get_api_id(self, url: str) -> int:
        """naive implementation of api id getter
        needed because resources are shared
        """
        splitted_url = url.split('/')
        return int(splitted_url[-2])  # -2 because of trailing slash

    def add_pokemon(self, api_results: dict):
        for pokemon in api_results:
            pokemon_data_response = requests.get(pokemon['url'])
            pokemon_data = pokemon_data_response.json()

            api_id = self.get_api_id(pokemon['url'])
            new_pokemon, _ = Pokemon.objects.get_or_create(
                api_id=api_id, name=pokemon['name'], weight=pokemon_data['weight']
            )

            self.add_ability(new_pokemon, pokemon_data)
            self.add_form(new_pokemon, pokemon_data)
            self.add_move(new_pokemon, pokemon_data)
            self.add_stat(new_pokemon, pokemon_data)
            self.add_type(new_pokemon, pokemon_data)

            new_pokemon.save()

            print(f"pokemon {pokemon['name']} added, api_id {api_id}")

    def add_ability(self, pokemon: Pokemon, pokemon_data: dict):
        for one in pokemon_data['abilities']:
            new_ability, _ = Ability.objects.get_or_create(
                api_id=self.get_api_id(one['ability']['url']), name=one['ability']['name']
            )

            pokemon.abilities.add(new_ability)

    def add_form(self, pokemon: Pokemon, pokemon_data: dict):
        for one in pokemon_data['forms']:
            new_form, _ = Form.objects.get_or_create(api_id=self.get_api_id(one['url']), name=one['name'])

            pokemon.forms.add(new_form)

    def add_move(self, pokemon: Pokemon, pokemon_data: dict):
        for one in pokemon_data['moves']:
            new_move, _ = Move.objects.get_or_create(
                api_id=self.get_api_id(one['move']['url']), name=one['move']['name']
            )

            pokemon.moves.add(new_move)

    def add_stat(self, pokemon: Pokemon, pokemon_data: dict):
        for one in pokemon_data['stats']:
            new_stat, _ = Stat.objects.get_or_create(
                api_id=self.get_api_id(one['stat']['url']), name=one['stat']['name']
            )

            pokemon.stats.add(new_stat)

    def add_type(self, pokemon: Pokemon, pokemon_data: dict):
        for one in pokemon_data['types']:
            new_type, _ = Type.objects.get_or_create(
                api_id=self.get_api_id(one['type']['url']), name=one['type']['name']
            )

            pokemon.types.add(new_type)
