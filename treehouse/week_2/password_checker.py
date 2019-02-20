# WARNING: don't try this at home

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
