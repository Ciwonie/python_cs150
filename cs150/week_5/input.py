import random

# a = float(input("Type in a number: "))
# b = float(input("Type a second number: "))
# sum = a + b

# print(" The sum of " + str(a) + " + " + str(b) + " is " + str(sum))

# incompass the input within a while loop
# This while loop continues until your guess number is equal to the number generated

myRandomNumber = random.randint(1, 10)
print(myRandomNumber)

# this is a sample of how to append elements within a while loop
a = [2, 5, 8, 9, 6]
b = []

# This is a sample while loop that uses an incrementing number to break the loop
i = 0
while i < len(a):
    b.append(a[i]-1)
    i += 1

print(a)
print(b)

# This is a sample while loop that uses a boolean variable to break out of the loop
# A boolean can only be True or False
i = 0
myNumber = True
while myNumber == True:
    print(a[i])
    if a[i] == 8:
        myNumber = False
    i += 1
