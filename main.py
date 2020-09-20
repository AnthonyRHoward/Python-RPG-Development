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
playerName = ""
# end global vars
# start opening screen of the game.
# gets the players screen name.
playerName = input("What is your name, My Lord?:")
# stores the players class (Magic, Range or Melee)
playerClass = ""
# stores the players stats
magicAttack = 0
rangeAttack = 0
meleeAttack = 0
magicDefence = 0
rangeDefence = 0
meleeDefence = 0


# defines the stats window
def playerstats():
    print("")
    print("")
    print("Welcome to the Mighty Adventure of", playerName)
    print("")
    print("************")
    print(playerName, "Starting HP", playerHP)
    print(playerName, "Starting Money", playerMoney)
    print(playerName, "Starting Reputation", playerRep)
    print("************")
    print(playerName, "Magic Attack", magicAttack)
    print(playerName, "Magic Defence", magicDefence)
    print(playerName, "Range Attack", rangeAttack)
    print(playerName, "Range Defence", rangeDefence)
    print(playerName, "Melee Attack", meleeAttack)
    print(playerName, "Melee Defence", meleeDefence)
    print("************")
    print("")


playerstats()

playerClass = input("What is your style of choice? (Magic, Melee, Range):")

if playerClass == "Range":
    rangeAttack = random.randint(1, 10)
    magicDefence = random.randint(1, 10)
    playerRep += random.randint(1, 5)
elif playerClass == "Magic":
    magicAttack = random.randint(1, 25)
    playerRep += random.randint(1, 3)
elif playerClass == "Melee":
    meleeAttack = random.randint(1, 10)
    rangeDefence = random.randint(1, 5)
    meleeDefence = random.randint(1, 5)
    playerRep += random.randint(1, 7)
else:
    print("No Class Selected")
    playerClass = input("What is your style of choice? (Magic, Melee, Range):")

playerstats()



