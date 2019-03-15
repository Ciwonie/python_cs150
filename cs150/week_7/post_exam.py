# QUESTION 1 - Write a program that adds up all the index and even values into a and prints out the final value.
a = [12, 34, 28, 96, 57, 105, 26]

mySum = 0
for index, element in enumerate(a):
    if index % 2 == 1 and element % 2 == 0:
        mySum += element
print(mySum)
print('==================================')

# QUESTION 2 - Write a program that prints the index and the value in a for each iteration
b = [12, 54, 13, 5, 17]
for index, value in enumerate(b):
    print('Index: {} Value: {}'.format(index, value))
print('==================================')

# Question 3 - Write a program using the range command that prints the values between 3 and 8
for x in range(3, 9):
    print(x)
print('==================================')

# Question 4 - Write a while loop that iterates over a, adding up each odd element of a into a variable sum. This loop exists only when the value is 20 or over. After the while loop, print out the value in sum.
c = [3, 5, 8, 10, 15, 18]
i = 0
sum = 0
while sum < 20:
    if c[i] % 2 == 1:
        sum += c[i]
    i += 1
print(sum)
print('==================================')

# Question 5 - Write a program that outputs the balue from the variables output1, output2, and output3. This program must use a loop that
# iterates the values in the list. Output1 is the sum of all even index numbers under 20, output2 is the sum of all odd index numbers under 20,
# and output3 is the sum of all the values that are over 20
output1 = 0
output2 = 0
output3 = 0
d = [1, 4, 6, 34, 12, 7, 5, 34, 12, 15]
for index, value in enumerate(d):
    if index % 2 == 0 and value < 20:
        output1 += value
    elif index % 2 == 1 and value < 20:
        output2 += value
    elif value > 20:
        output3 += value
print('Output1: ' + str(output1))
print('Output2: ' + str(output2))
print('Output3: ' + str(output3))
print('==================================')

# Question 6 - Write a function that will take in two variables e.g x,y if the sum is even then return the sum of the two variables, otherwise return 0


def evenFunction(x, y):
    if (x+y) % 2 == 0:
        return(x+y)
    else:
        return 0


print('Even Function: ' + str(evenFunction(5, 5)))
print('==================================')

# Question 7 - What is the output of this function
f = 20


def doSomething():
    f = 10


doSomething()
print('The value of f: ' + str(f))

print('==================================')
# Question 8 - Constructor

nameList = ['John', 'Peter', 'Mark']


class Faculty:
    facultyCount = 0

    def __init__(self, name):
        self.facultyName = name
        Faculty.facultyCount += 1


for i in nameList:
    newFaculty = Faculty(i)
    print('Faculty name: ' + str(newFaculty.facultyName))
    print('Faculty Count: ' + str(Faculty.facultyCount))
