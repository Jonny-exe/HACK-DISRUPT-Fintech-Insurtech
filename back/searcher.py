#!/usr/bin/python3
from get_data import get_classes
food, transport, electricity, clothes = get_classes()
def search(words):
    if type(words) == str:
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
    return search([word[:int(len(word) / 2)] for word in words])

print(search("aaaaaaaaaaaaa"))

