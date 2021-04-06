#!/usr/bin/env python3

"""Ricky Lucas || Making a custom if elif else program"""

import random

ranum1 = random.randint(0,5)
ranum2 = random.randint(0,5)
print(f"Welcome to High or Low!! the current number is: {ranum1} ")

if ranum2 > ranum1:
    status = "High"
elif ranum2 < ranum1:
    status = "Low"
else:
    status = "Tie"

playerinput = input("Is the next number High, Low or Tie: ")
print(f"The next number is {ranum2} - {status} ")

if playerinput == status:
    message = "You win!"
else:
    message = "Lewhewzeher!"
print(message)
