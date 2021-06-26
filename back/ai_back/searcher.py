#!/usr/bin/python3
from get_data import get_classes

word = "zapatilla azul"

food, transport, electricity, clothes = get_classes()

def search(words):
    words = words.split(" ")
    for i in food:
        for word in words:
            if word in i:
                return "food"

    for i in electricity:
        for word in words:
            if word in i:
                return "electricity"

    for i in transport:
        for word in words:
            if word in i:
                return "transport"

    for i in clothes:
        for word in words:
            if word in i:
                return "clothes"
    return None


print(search(word))
