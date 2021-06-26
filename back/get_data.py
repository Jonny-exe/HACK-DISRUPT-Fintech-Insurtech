#!/usr/bin/python3

from new_data import food, transport, electricity, clothes


def get_data():
    # X observation, class
    # Y action, result
    result = []
    # X  Y

    X = []
    X.extend(food)
    X.extend(transport)
    X.extend(electricity)
    Y = [0] * len(food) + [1] * len(transport) + [2] * len(electricity)
    return X, Y

def get_classes():
    return food, transport, electricity, clothes

def create_data():
    result = []
    # X  Y

    X = []
    X.extend(food)
    X.extend(transport)
    X.extend(electricity)
    Y = [0] * len(food) + [1] * len(transport) + [2] * len(electricity)
    result = []
    for i in range(len(Y)):
        result.append((X[i], Y[i]))
    return result


def get_clases():
    # TODO do this with average kg per month
    CLASSE = {
        "food": 7 / 3,  # kg per day
        "transport": 0.1,  # kg per kilometre
        # "gasoline": ,
        "electricity": 0.5,  # kg per kilometre per kW/h
    }
    return CLASSES
