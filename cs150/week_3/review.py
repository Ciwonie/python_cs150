# print even index values
# c = [12, 56, 78, 96, 45, 10]

# outputVal = 0

# for key, value in enumerate(c) :
#     if key % 2 == 1 :
#         print(key, value)
#         outputVal = outputVal + value

# print(outputVal)

# COMPARING
# >, >=, <, <=, !=

# WHILE LOOP

# x = 0
# while x < 10 :
#     print(x)
#     x = x + 1

k = [ 23, 56, 98, 12, 74, 5]

# A contains variables less than 10
a = [ ]
# Variables >= 10 but less than 20
b = [ ]
# Variables 20 or greater
c = [ ]

for element in k :
    if  element < 10 :
        a.append(element)
    elif element >= 10 and element < 20 :
        b.append(element)
    else : 
        c.append(element)

print(a)
print(b)
print(c)


