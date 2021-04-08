#!/usr/bin/env python3
"""This game has no OOP implementation"""

import random

# Create Player's dice
player1_dice = []
player2_dice = []

# Dice roll
for i in range(3):
  player1_dice.append(random.randint(1,6))
  player2_dice.append(random.randint(1,6))

# Run the game
print("Player 1 rolled" + str(player1_dice))
print("Player 2 rolled" + str(player2_dice))

if sum(player1_dice) == sum(player2_dice):
  print("Draw")
elif sum(player1_dice) > sum(player2_dice):
  print("Player 1 wins")
else:
  print("Player 2 wins")

