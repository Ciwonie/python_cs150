# INSTRUCTIONS
# This is a take home assignment - assigned on week 5, due week 6.
# From the  data file, and python file (check the notes folder  in the lesson link
# - studentRecord.csv, objectExample.py ) complete the class by reading in the gpa,
# print out all the student (gpa and name) and faculty instances (name and the research string).
# Also print out the number of students and the number of faculty.

studentSet = []
gpaSet = []
facultySet = []
researchTopicset = []

with open('studentRecord.csv') as csv_file:
    for count, line in enumerate(csv_file):
        if count == 0:
            continue
        lineValues = line.rstrip('\n').strip('-').split(',')
        # The following two lines will show how lineVariable works:
        # print("lineValues Variable : " + str(lineValues))
        # print("count: " + str(count))

        for index, value in enumerate(lineValues):
            if index == 0:
                studentSet.append(value)
            elif index == 1:
                gpaSet.append(float(value))
            elif index == 2:
                facultySet.append(value)
            else:
                researchTopicset.append(value)

# print(studentSet)
# print(gpaSet)
# print(facultySet)
# print(researchTopicset)

students = []
facultyMembers = []


class Student:

    studentCount = 0
    gpaSum = 0

    # First constructor function for students and gps
    def __init__(self, name, gpa):
        self.studentName = name
        self.studentGPA = gpa
        Student.studentCount += 1
        Student.gpaSum += gpa

    # def setGPA(self, gpa):
    #     self.studentGPA = gpa
    #     Student.gpaSum += gpa


class Faculty:

    facultyCount = 0

    def __init__(self, name, research):
        self.facultyName = name
        self.researchName = research
        Faculty.facultyCount += 1


for index, value in enumerate(facultySet):
    newFaculty = Faculty(value, researchTopicset[index])
    facultyMembers.extend([newFaculty.facultyName, newFaculty.researchName])


for index, value in enumerate(studentSet):
    newStudent = Student(value, gpaSet[index])
    # newStudent.setGPA(gpaSet[index])
    students.extend([newStudent.studentName, newStudent.studentGPA])

    # students.append(str(newStudent.studentName) +
    #                 " " + str(newStudent.studentGPA))


print('Number of students: ' + str(Student.studentCount))
print('The average gpa is: ' + str(Student.gpaSum / Student.studentCount))

print(students)

print('=========================')

print('Number of faculty: ' + str(Faculty.facultyCount))
print(facultyMembers)
