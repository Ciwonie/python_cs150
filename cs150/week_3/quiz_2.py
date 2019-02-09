a = [72, 15, 64, 33, 24, 98, 5, 53, 112]

# Problem 1: Print all the even numbers in a

for i in a :
    if i % 2 == 0:
        print(i)

# Problem 2: 

output1 = 0
output2 = 0
output3 = 0

for key, value in enumerate(a) :
    if key % 5 == 0 :
        output1 = output1 + value
    elif key % 3 == 0 and key % 5 != 0 :
        output2 = output2 + value
    else :
        output3 = output3 + value

print("output1: {}".format(output1))
print("output2: {}".format(output2))
print("output3: {}".format(output3))

# Problem 3 

x = 0
while x <= 10:
    if x == 2 or x ==5 or x == 7 :
        x += 1
        continue
    print(x)
    x +=1

# Problem 4

# sum1 = []
# sum2 = []
# for key, value in enumerate(a) :
#     if key == index1:
#         for element in value:
#             sum1.append(element)
#     elif key == index2 :
#         for element in value:
#             sum2.append(element)