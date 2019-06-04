# Packing and Unpacking tuples in python with a multiplication function


def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total
