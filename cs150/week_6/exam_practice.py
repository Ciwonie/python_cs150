# PRACTICE 1 - Range command
for x in range(1, 10):
    # this is going to print the numbers 1-9
    print(x)
print('----------------------------------')
print('----------------------------------')

# PRACETICE 2 - Enumeration Operation to print even or odds
a = [1, 2, 5, 6, 7, 8, 9]
b = 0
c = 0

for key, value in enumerate(a):
    if key % 2 == 0:
        b += value
    if value % 2 == 1:
        c += value

print('value of b: ' + str(b))
print('value of c: ' + str(c))
print('----------------------------------')
print('----------------------------------')

# PRACTICE 3 - While loop questions:
d = [2, 4, 6, 7, 8, 3, 12, 15, 24, 42]
i = 0
summation = 0
while summation < 20:
    if d[i] % 2 == 0:
        summation = summation + d[i]
        i += 1
    else:
        i += 1
print('Summation: ' + str(summation))

print('----------------------------------')
print('----------------------------------')

# Another while loop question
e = [1, 4, 5, 6, 73, 65, 12, 34, 15, 78, 15]
z = 0
evenOutputs = 0
oddOutputs = 0
while z < len(e):
    if e[z] % 2 == 0:
        evenOutputs += e[z]
        z += 1
    elif e[z] % 2 == 1:
        oddOutputs += e[z]
        z += 1

print('Even Output: ' + str(evenOutputs))
print('Odd Output: ' + str(oddOutputs))

print('----------------------------------')
print('----------------------------------')

# PRACTICE 4 - Functions
f = 10


def whatDoesThisDo():
    f = 3


whatDoesThisDo()
print('f should equal: ' + str(f))

print('----------------------------------')
print('----------------------------------')

# PRACTICE 5 - Biblical constructors of the holy trinity
nameList = ['John', 'Peter', 'Mark']


class Student:

    def __init__(self, name):
        self.biblicalName = name


for i in nameList:
    studentInstance = Student(i)
    print('Constructor: ' + str(studentInstance.biblicalName))
