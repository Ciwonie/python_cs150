# Tuples are mostly immutable.
# I can change tuples if there's a list within the tuple.
# Tuples are good for their smaller memory footprint.
# Tuples can unpack, but they don't have key|value pairs.
# a single * can pack a tuple in a function

# packing tuple calculator


def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total
