#!/usr/bin/env python3
"""RLucas | Tuesday Morning Review
Parse data from ISS now displaying ISS's LAT and LONG"""    
#required for datetime
import datetime
# required to make HTTP requests
import requests

def main():
    #catch user input, ask pokemon which pokemon
    pokemon = input("Which pokemon would you like to view? ")
    # api goes here
    # example:
    api = "https://pokeapi.co/api/v2/pokemon/"   # <--- you have to fill in this!

    # sent HTTP GET and create resp, a response object
    resp = requests.get(api + pokemon)

    # respdata is the JSON attached to our 200+JSON response
    # converted to pythonic list and dictonaries
    respdata = resp.json()
    # spend some time working with dataset
    # see if you can return the data in an interesting format
    # (make it more readable)
    print(respdata.get("abilities"))


main()
