# # Developer Jonathan Cirone
# # Project 1

# print("Hello, world!")

# numberSet = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# # counter = 10
# # for i in range(10) : 
# #     print(counter)
# #     counter = counter - 1

# # for i in numberSet : 
# #     if i % 2 == 1 :
# #         print("odd number found", i)


# # fibinocci number set project
# a = 0
# b = 1
# c = 0

# for i in range(10) :
#     if i == 0 : 
#         print(a)
#         continue
#     elif i == 1 : 
#         print(b)
#         continue
#     c = a + b
#     a = b
#     b = c
#     print(c)
# # end of fibinocci project1


# # Start of Project 2
# print("Project 2")
# newSet = [0,2,5,7,9,11,16,56,3]
# finalOutput = 0
# for index, i in enumerate(newSet) : 
#     if index % 2 == 0 :
#         finalOutput = finalOutput + i

# print(finalOutput)
# #End of Project 2

# #Start of Splicing
# nextSet = [0,12,5,7,89,12,5]
# anotherSet = nextSet[2:]
# thirdSet = nextSet[:3]

# print("Nextset", nextSet)
# print("anotherSet", anotherSet)
# print("thirdSet", thirdSet)

# nestedSet = [12, 45, [0,1], "red", "green", [34, "banana", [23, 56]], 5]

# print(nestedSet[5][2][0])

#Project 4
a = 5
b = 3 

for i in range(b) :
    a = a + i

for i in range(a) : 
    for j in range(b) :
        print(i,j)





