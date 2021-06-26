#!/usr/bin/python3
import csv
from searcher import search
from io import StringIO

def string_to_file(string):
    f = StringIO(string)
    reader = csv.DictReader(f)
    return reader

def get_sections(reader):
    result = []
    for i in reader:
        # print(i["item"], search(i["item"]))
        result.append(search(i["item"]))
    return dict(result)

