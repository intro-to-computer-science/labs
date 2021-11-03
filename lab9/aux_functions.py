import json

def getAllPokemons():
    f = open('pokemon.json')
    return json.load(f)

def getPokemonByName(name):
    pokedex = getAllPokemons()
    for pkmn in pokedex:
        if pkmn["name"] == name:
            return pkmn

def getLocationsByName(name):
    pkmn = getPokemonByName(name)
    coordx, coordy = [], []
    try:
        coordx = pkmn["coordx"]
        coordy = pkmn["coordy"]
    except:
        pass
    return coordx, coordy

def getTypesByName(name):
    pkmn = getPokemonByName(name)
    return pkmn["type"]

def getWeaknessesByName(name):
    pkmn = getPokemonByName(name)
    return pkmn["weaknesses"]