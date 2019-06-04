numbers = list(range(0, 20))
print(numbers)


def first_4(iterable):
    return iterable[:4]


output = 0
for i in range(2):
    k = 0
    for j in range(3):
        k += 1
    output += k
print(output)


# Sillycase is designed to take in a string and convert the first half to lowercase and the second half to upper
def sillycase(string):
    separated = list(string)
    lower_half = []
    upper_half = []
    print(len(string)/2)

    for key, value in enumerate(separated):
        if key < round(len(string)/2):
            lower_half.extend(value)
        else:
            upper_half.extend(value)
    return("".join(lower_half).lower() + "".join(upper_half).upper())
