import requests 

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)

    if response.status_code == 200:
        planets = response.json()['bodies']

        planet_list = []
        for planet in planets:
            if planet['isPlanet']:
                name = planet.get('englishName')
                mass = planet['mass']['massValue']
                orbit_period = planet.get('sideralOrbit')
                planet_list.append({
                    'name': name,
                    'mass': mass,
                    'orbit_period': orbit_period
                })
                print(f"Planet: {name}\nMass: {mass}\nOrbit Period: {orbit_period} days\n")
        return planet_list

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda planet: planet['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']


planets = fetch_planet_data()

if planets:
    name_heavy, mass_heavy = find_heaviest_planet(planets)
    print(f"The heaviest planet is {name_heavy} with a mass of {mass_heavy} kg.")