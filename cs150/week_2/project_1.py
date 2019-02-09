a = [ 7, 23, 56, 128, 92, 48, 12, 32, 95 , 96 , 74, 93]
result1 = 1
result2 = 1
result3 = 0

for i in range(1, len(a)+1):
    if(i % 4 == 0):
        result1 *= a[i-1]
    elif(i % 3 == 0):
        result2 *= a[i-1]
    elif(i % 2 == 0):
        result3 += a[i-1]

print(result1)
print(result2)
print(result3)

# or we can write it this way 

# Instructions
# Given the following input  a = [ 7, 23, 56, 128, 92 48, 12, 32, 95 , 96 , 74, 93]
# 1 multiply every fourth input in a. put the result in result1. Print out result1.  So result1 will have the product 128 * 32 * 93  
# 2. multiply every third input in a (only if it is not the fourth input), put the result in result2. Print out result2.  So result2  will have the product of 56x48x95
# 3. add every second input in a (only if it is not the fourth or third input) put the result in result3. Print out result3.  So result3  will have the result 23 + 96

resultX = 1
resultY = 1
resultZ = 0

for key, value in enumerate(a):
    if key == 3 or key == 7 or key == 11:
        resultX = resultX * value
    elif key == 2 or key == 5 or key == 8:
        resultY = resultY * value
    elif key == 1 or key == 9:
        resultZ = resultZ + value

print("result X: {}".format(resultX))
print("result Y: {}".format(resultY))
print("result Z: {}".format(resultZ))
