import click
import requests

def __get_pokemon_info(pokemon_name):
    """
    Gets all the necessary information through the API using GET requests.
    """
    try:
        url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon_name
        json = requests.get(url).json()

        height = json['height']
        weight = json['weight']
        abilities = []

        ability_items = json['abilities']
        for item in ability_items:
            ability_link = item['ability']['url']
            ability_name = item['ability']['name']
            ability_info = requests.get(ability_link).json()['effect_entries'][1]['short_effect']

            abilities.append({
                'spell' : ability_name,
                'info'  : ability_info,
            })

        pokemon_info = {
            'name'      : pokemon_name,
            'height'    : height,
            'weight'    : weight,
            'abilities' : abilities,
        }
    except ValueError:
        print('Error. No such pokemon was found.')
        return

    return pokemon_info


def __print_info(info):
    """
    Print all necessary infomation.
    """

    print('=' * 100)
    print(f"You get {info['name']}! Height equals {info['height']} and weight equals {info['weight']}.\n" 
                + f"There {len(info['abilities'])} abilities:")

    for ability in info['abilities']:
        print(f"\nSpell: {ability['spell']}\nDescription: {ability['info']}")


@click.command()
@click.argument('name')
def __main(name):
    """
    This module provides general information about the selected pokemon by name.
    """
    get_pokemon_by_name(name)
    

def get_pokemon_by_name(name):
    info = __get_pokemon_info(name.lower())
    if info: __print_info(info)


if __name__ == "__main__":
    __main()