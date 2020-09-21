""" Created by Anthony Probert
    Attempt #1 at an Adventure Game
    Written in Python. """

import random
import settings


def currenttasks():
    settings.playerInput = ""
    settings.playerInput = input("What would you like to do?")
    playersaid()


def monsterbonus():
    if settings.monstersKilled == 10:
        settings.playerHP += 10
    elif settings.monstersKilled == 20:
        settings.playerHP += 15
    elif settings.monstersKilled == 30:
        settings.playerHP += 20


def monsterstats():
    if settings.playerClass == "Range" and settings.activeMonster == "Rat":
        settings.enemyAttack = random.randint(1, 2)
        settings.playerMoney += random.randint(0, 1)
    elif settings.playerClass == "Magic" and settings.activeMonster == "Rat":
        settings.enemyAttack = random.randint(1, 2)
        settings.playerMoney += random.randint(0, 1)
    elif settings.playerClass == "Melee" and settings.activeMonster == "Rat":
        settings.enemyAttack = random.randint(1, 2)
        settings.playerMoney += random.randint(0, 1)
    elif settings.playerClass == "Range" and settings.activeMonster == "Dog":
        settings.enemyAttack = random.randint(1, 2)
        settings.playerMoney += random.randint(0, 1)
    elif settings.playerClass == "Magic" and settings.activeMonster == "Dog":
        settings.enemyAttack = random.randint(1, 3)
        settings.playerMoney += random.randint(0, 1)
    elif settings.playerClass == "Melee" and settings.activeMonster == "Dog":
        settings.enemyAttack = random.randint(1, 2)
        settings.playerMoney += random.randint(0, 1)
    elif settings.playerClass == "Range" and settings.activeMonster == "Dragon":
        settings.enemyAttack = random.randint(1, 4)
        settings.playerMoney += random.randint(0, 5)
    elif settings.playerClass == "Magic" and settings.activeMonster == "Dragon":
        settings.enemyAttack = random.randint(1, 6)
        settings.playerMoney += random.randint(0, 5)
    elif settings.playerClass == "Melee" and settings.activeMonster == "Dragon":
        settings.enemyAttack = random.randint(1, 3)
        settings.playerMoney += random.randint(0, 5)
    elif settings.playerClass == "Range" and settings.activeMonster == "Human":
        settings.enemyAttack = random.randint(1, 6)
        settings.playerMoney += random.randint(0, 3)
    elif settings.playerClass == "Magic" and settings.activeMonster == "Human":
        settings.enemyAttack = random.randint(1, 3)
        settings.playerMoney += random.randint(0, 3)
    elif settings.playerClass == "Melee" and settings.activeMonster == "Human":
        settings.enemyAttack = random.randint(1, 2)
        settings.playerMoney += random.randint(0, 3)
    elif settings.playerClass == "Range" and settings.activeMonster == "Druid":
        settings.enemyAttack = random.randint(1, 2)
        settings.playerMoney += random.randint(0, 2)
    elif settings.playerClass == "Magic" and settings.activeMonster == "Druid":
        settings.enemyAttack = random.randint(1, 3)
        settings.playerMoney += random.randint(0, 2)
    elif settings.playerClass == "Melee" and settings.activeMonster == "Druid":
        settings.enemyAttack = random.randint(1, 5)
        settings.playerMoney += random.randint(0, 2)
    elif settings.playerClass == "Range" and settings.activeMonster == "Guard":
        settings.enemyAttack = random.randint(1, 3)
        settings.playerMoney += random.randint(0, 9)
    elif settings.playerClass == "Magic" and settings.activeMonster == "Guard":
        settings.enemyAttack = random.randint(1, 3)
        settings.playerMoney += random.randint(0, 9)
    elif settings.playerClass == "Melee" and settings.activeMonster == "Guard":
        settings.enemyAttack = random.randint(1, 2)
        settings.playerMoney += random.randint(0, 9)
    else:
        print("Error, I don't have that combination in my database.")


def attack():
    settings.activeMonster = random.choice(settings.possibleMonsters)
    monsterstats()
    settings.playerHP -= settings.enemyAttack
    print("You lost", settings.enemyAttack, "HP", "while killing a", settings.activeMonster)
    monsterbonus()
    if settings.playerHP <= 0:
        print("You died while killing", settings.activeMonster)
        exit(0)
    else:
        settings.monstersKilled += 1
        settings.activeMonster = ""


def playerstats():
    print("")
    print("Welcome to the Mighty Adventure of", settings.playerName)
    print("")
    print("************")
    print("Health Points", settings.playerHP)
    print("Gold Coins", settings.playerMoney)
    print("Reputation", settings.playerRep)
    print("************")
    print("Magic Attack", settings.magicAttack)
    print("Magic Defence", settings.magicDefence)
    print("Range Attack", settings.rangeAttack)
    print("Range Defence", settings.rangeDefence)
    print("Melee Attack", settings.meleeAttack)
    print("Melee Defence", settings.meleeDefence)
    print("************")
    print("Monsters Killed", settings.monstersKilled)
    print("************")
    print("")


def postfightstats():
    print("")
    print("************")
    print("Health Points", settings.playerHP)
    print("Gold Coins", settings.playerMoney)
    print("Reputation", settings.playerRep)
    print("Monsters Killed", settings.monstersKilled)
    print("************")
    print("")


def playersaid():
    if settings.playerInput == "Attack":
        attack()
        postfightstats()
        currenttasks()
    elif settings.playerInput == "Stats":
        playerstats()
        currenttasks()
    elif settings.playerInput == "Shops":
        for i in settings.shop:
            print(i, end=" ")
            print("")
        currenttasks()
    elif settings.playerInput == "quit":
        exit(0)
    else:
        currenttasks()


def playerclass():
    if settings.playerClass == "Range":
        settings.rangeAttack = random.randint(1, 10)
        settings.magicDefence = random.randint(1, 10)
        settings.playerRep += random.randint(1, 5)
        settings.playerMoney = random.randint(1, 25)
    elif settings.playerClass == "Magic":
        settings.magicAttack = random.randint(1, 25)
        settings.playerRep += random.randint(1, 3)
        settings.playerMoney = random.randint(1, 25)
    elif settings.playerClass == "Melee":
        settings.meleeAttack = random.randint(1, 10)
        settings.rangeDefence = random.randint(1, 5)
        settings.meleeDefence = random.randint(1, 5)
        settings.playerRep += random.randint(1, 7)
        settings.playerMoney = random.randint(1, 25)
    else:
        print("No Class Selected")
        settings.playerClass = input("What is your style of choice? (Magic, Melee, Range):")


settings.playerClass = input("What is your style of choice? (Magic, Melee, Range):")

playerclass()
playerstats()
currenttasks()
