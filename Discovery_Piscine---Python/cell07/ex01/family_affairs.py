#!/usr/bin/env python3

def find_the_redheads(dictionary):
    return list(filter(lambda key: dictionary[key] == "red", dictionary.keys()))

dupont_family =     {
                        "florian": "red",
                        "marie": "blond",
                        "virginie": "brunette",
                        "david": "red",
                        "franck": "red"
                    }

print(find_the_redheads(dupont_family))
