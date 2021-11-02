import matplotlib.pyplot as plt
import json

def getPokemonByName(name):
    f = open('pokemon.json')
    pokedex = json.load(f)
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

def ejercicio1():
    dic = {}
    f = open('pokemon.json')
    pokedex = json.load(f)
    for pkmn in pokedex:
        # Si no saben diccionarios, les podemos dar la funcion getTypesByName que les retorna la lista de tipos
        for t in pkmn["type"]:
            if t not in dic:
                dic[t] = 1
            else:
                dic[t] += 1

    print(dic)

    keys = dic.keys()
    values = dic.values()

    plt.bar(keys, values, color = ['forestgreen', 'purple', 'red', 'skyblue', 'dodgerblue', 'greenyellow', 'lightgray', 'yellow', 'darkgoldenrod', 'sienna', 'fuchsia', 'maroon', 'cyan', 'slateblue', 'midnightblue'])
    plt.show()



def ejercicio2():
    dic = {}
    f = open('pokemon.json')
    pokedex = json.load(f)
    vec = []
    for i in range(9):
        # Si no saben diccionarios pueden usar la funcion get weaknesses by name
        vec.append(len(pokedex[i]["weaknesses"]))

    plt.plot([i for i in range(1,10)], vec, 'o')
    plt.show()

def ejercicio3():
    unox, unoy = getLocationsByName("Articuno")
    dosx, dosy = getLocationsByName("Zapdos")
    tresx, tresy = getLocationsByName("Moltres")



    im = plt.imread('Kanto.png')
    implot = plt.imshow(im)

    plt.plot(unox, unoy,'o', color="cyan")
    plt.plot(dosx, dosy,'o', color="yellow")
    plt.plot(tresx, tresy,'o', color="red")

    plt.show()

def ejercicio4():
    magix, magiy = getLocationsByName("Magikarp")

    im = plt.imread('Kanto.png')
    implot = plt.imshow(im)

    plt.plot(magix, magiy,'o', color="purple")

    plt.show()

ejercicio2()