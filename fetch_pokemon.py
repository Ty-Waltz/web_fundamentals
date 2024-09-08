import requests
import json

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error finding pokemon: {pokemon_name}")

def display_pokemon_info(pokemon_data):
    if pokemon_data:
        name = pokemon_data['name']
        abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
        print(f"Name: {name}")
        print("Abilities:", ", ".join(abilities))

def calculate_weight(pokemon_list):
    weight = 0
    for pokemon_data in pokemon_list:
        weight += pokemon_data['weight']
    return weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_list = [fetch_pokemon_data(name) for name in pokemon_names]

for pokemon_data in pokemon_list:
    display_pokemon_info(pokemon_data)

pikachu_data = fetch_pokemon_data("pikachu")
display_pokemon_info(pikachu_data)

weight = calculate_weight(pokemon_list)
print(f"The average weight is {weight}")