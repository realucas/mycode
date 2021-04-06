#!/usr/bin/env python3

"""RLucas | Tuesday Morning Review
Parse data from ISS now displaying ISS's LAT and LONG"""

from datetime import datetime

now = datetime.now()
#capture source data
issnow =  {"message": "success", "timestamp": 1617722483, "iss_position": {"longitude": "162.5270", "latitude": "-50.1455"}}
print(f"At, {now} this iss is:")
longit = issnow.get("iss_position").get("longitude")
latit = issnow.get("iss_position").get("latitude")

print(f"Longitude - {longit}")
print(f"Latitude - {latit}")


