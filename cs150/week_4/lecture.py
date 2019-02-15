# goal is to read a separate file, read it, and organize the set of data
studentSet = []
facultySet = []
gpaSet = []
researchTopicSet = []

with open('studentRecord.csv') as csv_file :
    for count, line in enumerate(csv_file) :
        if count == 0 :
            continue
        lineValues = line.rstrip('\n').strip('-').split(',')
        # The following two lines will show how lineVariable works:
        # print("lineValues Variable : " + str(lineValues))
        # print("count: " + str(count))
        for index, word in enumerate(lineValues) :
            if index == 0 :
                studentSet.append(word)
            elif index == 1 :
                gpaSet.append(float(word))
            elif index == 2 :
                facultySet.append(word)
            else :
                researchTopicSet.append(word)

print(studentSet)
print(gpaSet)
print(facultySet)
print(researchTopicSet)


students = []
facultyMembers = []

class Student :

    studentCount = 0
    gpaSum = 0

    #constructor function - creates the object (instance)
    def __init__(self, name) :
        self.studentName = name
        Student.studentCount = Student.studentCount + 1

    def setGPA(self, gpa) :
        self.studentGPA = gpa
        Student.gpaSum += gpa


for index, item in enumerate(studentSet) :
    newStudent = Student(item)
    newStudent.setGPA(gpaSet[index])
    
    print(newStudent.studentName, newStudent.studentGPA)

print('The number of students ' + str(Student.studentCount))
print("The average gpa is " + str(Student.gpaSum / Student.studentCount))
