from math import trunc
from random import randint

money = 0
bitcoin = 0
multiplier = 1
PCpower = 0


def titleScreen():
    choice = input("Welcome to Bitcoin Mining Simulator! Want to play? (Y/N)")
    if choice == "Y":
        bitcoinMine()


def bitcoinMine():
    global money
    global bitcoin
    global PCpower
    print("-------------------------------------------------------------------------")
    print("You have " + str(money) + " dollars and " + str(bitcoin) + " Bitcoin")
    decision = input("What would you like to do?  1) Mine Bitcoin  2) Cool PC Down  3) Sell Bitcoin")
    if decision == "1":
        minedBitcoin = randint(0, 3)
        print("You mined " + str(minedBitcoin) + " bitcoin")
        bitcoin += minedBitcoin
        PCpower += 1
    if decision == "2":
        print("You let your PC Rest")
        PCpower -= 1
    if decision == "3":
        moneyMade = bitcoin * 100
        print("You sold all your bitcoin and made " + str(moneyMade) + " dollars")
        money += moneyMade
        PCpower += 1
    if checkIfExplode():
        print(
            "You got too greedy and your PC blew up, which made you lose all your bitcoin. But at least you made " + str(
                money) + " dollars")
    else:
        bitcoinMine()


def checkIfExplode():
    global PCpower
    if PCpower >= 3:
        return True
    else:
        return False


titleScreen()
