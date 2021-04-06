#!/usr/bin/env python3
"""RLucas | Tuesday Morning Review
Parse data from ISS now displaying ISS's LAT and LONG"""    
#required for datetime
import datetime
# required to make HTTP requests
import requests

def main():

    # api goes here
    # example:
    api = "http://api.open-notify.org/iss-now.json"   # <--- you have to fill in this!

    # sent HTTP GET and create resp, a response object
    resp = requests.get(api)

    # respdata is the JSON attached to our 200+JSON response
    # converted to pythonic list and dictonaries
    issnow = resp.json()
    # spend some time working with dataset
    # see if you can return the data in an interesting format
    # (make it more readable)
    now = datetime.datetime.now()
    print(f"At, {now} this iss is:")
    longit = issnow.get("iss_position").get("longitude")
    latit = issnow.get("iss_position").get("latitude")

    print(f"Longitude - {longit}")
    print(f"Latitude - {latit}")


main()
