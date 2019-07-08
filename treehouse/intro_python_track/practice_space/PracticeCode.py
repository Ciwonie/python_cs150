# CHALLENGE 1: FizzBuzz in Python
# ************************************************************************** #
# name = input("Hello, Please enter your name:  ")
# number = int(input("Please enter an integer for FizzBuzz:  "))

# print("Hey {}! \nThe number {} ...".format(name, number))

# is_fizz = number % 3 == 0
# is_buzz = number % 5 == 0

# if is_fizz and is_buzz:
#     print("is a FizzBuzz number.")
# elif is_fizz:
#     print("is a Fizz number.")
# elif is_buzz:
#     print("is a Buzz number.")
# else:
#     print("is neither a fizzy or buzzy number.")


# CHALLENGE 2: Use a varios and loops to print specific numbers
# ************************************************************************** #
# numberSet = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# counter = 10
# for i in range(10):
#     print(counter)
#     counter = counter - 1

# for i in numberSet:
#     if i % 2 == 1:
#         print("odd number found: ", i)

# a = 0
# b = 1
# c = 0

# for i in range(10):
#     if i == 0:
#         print(a)
#         continue
#     elif i == 1:
#         print(b)
#         continue
#     c = a + b
#     a = b
#     b = c
#     print(c)

# CHALLENGE 3: Using Try/Raise to control input of data
# ************************************************************************** #

# import math


# def split_check(total, number_of_people):
#     if number_of_people <= 1:
#         raise ValueError("More than 1 person is required to split the check")
#     return math.ceil(total/number_of_people)


# try:
#     total_due = float(input("What is the total bill? "))
#     number_of_people = int(input("How many people are splitting? "))
#     amount_due = split_check(total_due, number_of_people)
# except ValueError as err:
#     print("Oh no! That's not valid. Try again ...")
#     print("{}".format(err))
# else:
#     print("Each person owes ${}".format(amount_due))


# CHALLENGE 4: Password Checker
# **************************************************************************

import sys

MASTER_PASSWORD = 'opensesame'

password = input("Please enter the super secret password: ")
attempt_count = 0

while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again: ")
    attempt_count += 1
print("Welcome to secret town!")
