""" Created by Anthony Probert
    Attempt #1 at an Adventure Game
    Written in Python. """
import random
# start global vars
# player starts with 20 hp at the beginning of the game.
playerHP = 20
# player stats the game with a random amount of $ between 1-25.
playerMoney = random.randint(1, 25)
# player starts the game with no reputation.
playerRep = 0
# stores player name
playerName = "asdf"
# end global vars
# start opening screen of the game.

print("Welcome to Olaf's Big Adventure.")
print("")
print("************")
print("Olaf's Starting HP", playerHP)
print("Olaf's Starting Money", playerMoney)
print("Olaf's Starting Reputation", playerRep)
print("************")
print("")

