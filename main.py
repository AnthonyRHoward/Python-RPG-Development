""" Created by Anthony Probert
    Attempt #1 at an Adventure Game
    Written in Python. """
import random


# start vars
playerHP = 20
playerMoney = 0
playerRep = 0
playerName = ""
playerName = input("What is your name, My Lord?:")
playerClass = ""
enemyAttack = 0
magicAttack = 0
rangeAttack = 0
meleeAttack = 0
magicDefence = 0
rangeDefence = 0
meleeDefence = 0
monstersKilled = 0
playerInput = ""
possibleMonsters = ["Rat", "Dog", "Dragon", "Human", "Shawman", "Druid", "Guard"]
activeMonster = ""
shop = ["Dagger 6 Gold", "Shield 10 Gold", "Cape 4 Gold", "Whip 25 Gold"]
# end Vars


def currenttasks():
    global playerInput
    playerInput = ""
    playerInput = input("What would you like to do?")
    playersaid()


def attack():
    global enemyAttack, monstersKilled, playerHP, possibleMonsters, activeMonster
    activeMonster = random.choice(possibleMonsters)
    enemyAttack = random.randint(1, 5)
    print("You lost", enemyAttack, "HP", "while killing a", activeMonster)
    playerHP -= enemyAttack
    if playerHP <= 0:
        print("You died while killing", activeMonster)
        exit(0)
    else:
        monstersKilled += 1
        activeMonster = ""


def playerstats():
    print("")
    print("")
    print("Welcome to the Mighty Adventure of", playerName)
    print("")
    print("************")
    print(playerName, "Health Points", playerHP)
    print(playerName, "Gold Coins", playerMoney)
    print(playerName, "Reputation", playerRep)
    print("************")
    print("Magic Attack", magicAttack)
    print("Magic Defence", magicDefence)
    print("Range Attack", rangeAttack)
    print("Range Defence", rangeDefence)
    print("Melee Attack", meleeAttack)
    print("Melee Defence", meleeDefence)
    print("************")
    print("Monsters Killed", monstersKilled)
    print("************")
    print("")


def playersaid():
    global playerInput
    if playerInput == "Attack":
        attack()
        playerstats()
        currenttasks()
    elif playerInput == "stats":
        playerstats()
        currenttasks()
    elif playerInput == "shops":
        for i in shop:
            print(i, end=" ")
            print("")
        currenttasks()
    elif playerInput == "quit":
        exit(0)
    else:
        currenttasks()


def playerclass():
    global playerClass, rangeAttack, rangeDefence, magicDefence, magicAttack, meleeDefence, meleeAttack, \
        playerRep, playerMoney
    if playerClass == "Range":
        rangeAttack = random.randint(1, 10)
        magicDefence = random.randint(1, 10)
        playerRep += random.randint(1, 5)
        playerMoney = random.randint(1, 25)
    elif playerClass == "Magic":
        magicAttack = random.randint(1, 25)
        playerRep += random.randint(1, 3)
        playerMoney = random.randint(1, 25)
    elif playerClass == "Melee":
        meleeAttack = random.randint(1, 10)
        rangeDefence = random.randint(1, 5)
        meleeDefence = random.randint(1, 5)
        playerRep += random.randint(1, 7)
        playerMoney = random.randint(1, 25)
    else:
        print("No Class Selected")
        playerClass = input("What is your style of choice? (Magic, Melee, Range):")


playerClass = input("What is your style of choice? (Magic, Melee, Range):")

playerclass()
playerstats()
currenttasks()



