#!/usr/bin/env python3

def array_of_names(dictionary):
    array = []
    for key in dictionary:
        array.append(key.capitalize() + " " + dictionary[key].capitalize())
    return array

persons =   {
                "jean": "valjean",
                "grace": "hopper",
                "xavier": "niel",
                "fifi": "brindacier"
            }

print(array_of_names(persons))
