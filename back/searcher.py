#!/usr/bin/python3
from get_data import get_classes, get_exact_classes

food, transport, transport_aereo, electricity, clothes, restaurants, onlineshopping = get_classes()
food_exact, transport_exact, transport_aereo_exact, electricity_exact, clothes_exact, restaurants_exact, onlineshopping_exact = (
    get_exact_classes()
)


def search(words, i=0):
    if i > 3:
        return None
    if type(words) == str:
        words = words.split(" ")

    # Food
    category = "Comida"
    a = check(words, food_exact, category, exact=True)
    if a != None:
        return a, category

    a = check(words, food, category, average=food_exact["Average"])
    if a != None:
        return a, category

    # Transport
    category = "Transporte"
    a = check(words, transport_exact, category, exact=True)
    if a != None:
        return a, category

    a = check(words, transport, category, average=transport_exact["Average"])
    if a != None:
        return a, category

    # Transport aereo
    category = "Transporte aereo"
    a = check(words, transport_aereo_exact, category, exact=True)
    if a != None:
        return a, category

    a = check(
        words, transport_aereo, category, average=transport_aereo_exact["Average"]
    )
    if a != None:
        return a, category

    # Electricity
    category = "Electricidad"
    a = check(words, electricity, category, average=electricity_exact["Average"])
    if a != None:
        return a, category

    # Clothes
    category = "Ropa"
    a = check(words, clothes, category, average=clothes_exact["Average"])
    if a != None:
        return a, category

    # Restaurants
    category = "Restaurantes"
    a = check(words, restaurants_exact, category, exact=True)
    if a != None:
        return a, category

    a = check(words, restaurants, category, average=restaurants_exact["Average"])
    if a != None:
        return a, category

    # Online shopping
    category = "Compras online"
    a = check(words, onlineshopping_exact, category, exact=True)
    if a != None:
        return a, category

    a = check(words, onlineshopping, category, average=onlineshopping_exact["Average"])
    if a != None:
        return a, category
    # return search([word[:int(len(word) / 2)] for word in words], i+1)
    return None, None


def check(words, category, name, average=0, exact=False):
    for i in category:
        for word in words:
            if word.lower() in i.lower():
                if exact:
                    return category[i]
                else:
                    return average
    return None


print(search("pan"))
