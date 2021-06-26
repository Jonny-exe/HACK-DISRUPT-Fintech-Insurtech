#!/usr/bin/python3
from data import (
    food,
    transport,
    transport_aereo,
    electricity,
    clothes,
    restaurants,
    food_exact,
    transport_exact,
    electricity_exact,
    clothes_exact,
    transport_aereo_exact,
    restaurants_exact,
)


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


def arr_strip(arr):
    if type(arr) == list:
        result = []
        for i in arr:
            result.append(i.strip(""))
        return result
    else:
        result = {}
        for i in arr:
            i_new = i.strip("")
            result[i_new] = arr[i]
        return result


def get_classes():
    return (
        arr_strip(food),
        arr_strip(transport),
        arr_strip(transport_aereo),
        arr_strip(electricity),
        arr_strip(clothes),
        arr_strip(restaurants),
    )


def get_exact_classes():
    return (
        arr_strip(food_exact),
        arr_strip(transport_exact),
        arr_strip(transport_aereo_exact),
        arr_strip(electricity_exact),
        arr_strip(clothes_exact),
        arr_strip(restaurants_exact),
    )


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
