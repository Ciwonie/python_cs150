# This project you are to create a slot based game. Your player starts out with a $500 account,
# and you have 10 tries to win more money. Your program has a list of 10 values within a list representing the 10 slot
# choices :  [ '200', 'Bankrupt', 'Extra Spin', '100', '150', '5000', '-300','50', '-500' ].
# Each iteration represents a spin that randomizes these slot choices. Before each spin you are asked to pick a slot location.
# Based on your picked slot location, if it is a monetary value, then you are to add or subtract that amount to your account.
# If "Bankrupt" then your account sets to 0, if "Extra Spin" the you are added an extra spin.
# If you type -1 from the prompt then you exit the while loop, and your program prints  out your account to show your winnings
# or losings !  The cost of each spin is 20 dollars.

# Each spin state what you gained or lossed and print out your current account.
# By Jonathan Cirone and Billy Tsak

import random

slotList = ["200", "Bankrupt", "Extra Spin", "100",
            "150", "5000", "-300", "50", "-100", "-50"]

count = 0
accountBalance = 500

while count < 10:

    count += 1
    print('Your current balance is: ${} \nYour current count is: {}'.format(
        accountBalance, count))

    randomIndices = random.sample(range(0, len(slotList)), len(slotList))

    newSlot = []

    for i in range(len(slotList)):
        newSlot.append(slotList[randomIndices[i]])

    # print(newSlot)

    slotLocation = int(input("Pick a slot (0-9). Input -1 to quit: "))
    print("================================================\n")

    if slotLocation == -1:
        print("Your winings: ${}".format(accountBalance))
        break

    accountBalance -= 20
    # print(newSlot)
    print("You received: " + newSlot[slotLocation])

    if (newSlot[slotLocation] == "Bankrupt"):
        accountBalance = 0
    elif (newSlot[slotLocation] == "Extra Spin"):
        count -= 1
    else:
        accountBalance += int(newSlot[slotLocation])

    # Iteration 1  -  slotList[3]   -200
    # Iteration 2  -  slotList[2] - 300
    # Iteration 3  -  slotList[0] - 100
    # Iteration 4  -  slotList[1]  - 100

    #slotSelection = int(input("Pick a slot (0,9) "))
    # Randomize the slots
    # @ Authors: Jonathan Cirone and Billy Tsak
    #value = slotList[slotSelection]
