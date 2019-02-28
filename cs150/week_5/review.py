# ------ Review for test ------ #

# Know the range command - EX: write a program using the range operator that will print a to b
for x in range(1, 10):
    print('range: ' + str(x))
print('----------------------------------')

# Enumerate operator - EX: write a program that sums all the even, odd, or the even index numbers
a = [1, 2, 5, 6, 7, 8, 9]
b = 0

for key, value in enumerate(a):
    # or if value % 2 == 0
    if key % 2 == 0:
        b += value

print('Enumerate: ' + str(b))
print('----------------------------------')

# While question - EX: A question encompassing if, elif, else. Write a while loop program that only prints out even numbers and exits the while loop when the sum of the numbers are over 20
c = [2, 4, 6, 7, 8, 3, 12, 15, 24, 42]
i = 0
summation = 0
while summation < 20:
    if c[i] % 2 == 0:
        summation = summation + c[i]
        i += 1
    else:
        i += 1
print('Summation: ' + str(summation))
print('----------------------------------')


# Another EX
d = [1, 4, 5, 6, 73, 65, 12, 34, 15, 78, 15]
# output1 - the sum of all odd indexed numbers
# output2 - the sum of all even indexed numbers

# Write a function that will add two numbers and return a sum


def addition(a, b):
    return a + b


print('addition function: ' + str(addition(10, 5)))
print('----------------------------------')


# What is the output of this function - The answer is 10
f = 10


def myFunction():
    f = 3


myFunction()
print('f equals: ' + str(f))
print('----------------------------------')


# Constructors - EX: student class, write a program that will create instances of John, Peter, and Mark--the holy trinity of bible dudes
# and print out the names from the instances

nameList = ["John", "Peter", "Mark"]


class Student:
    def __init__(self, name):
        self.student = name


for a in nameList:
    studentInstance = Student(a)
    print('Constructor name: ' + str(studentInstance.student))
