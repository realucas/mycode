#!/usr/bin/env python3

"""Ricky Lucas || Making a custom if elif else program"""

import random

def setup():
    ranum1 = random.randint(0,5)
    ranum2 = random.randint(0,5)
    if ranum2 > ranum1:
        status = "high"
    elif ranum2 < ranum1:
        status = "low"
    elif ranum2 == ranum1:
        status = "tie"

def main():
    setup()
    print(f"Welcome to High or Low!! the current number is: {ranum1} ")
    playerinput = input("Is the next number High, Low or Tie?: ")
    if playerinput.lower == status:
        message = "You win!"
    else:
        message = "Lewhewzeher!"
    print(f"The next number is {ranum2} - {status} ")
    print(message)
main()
