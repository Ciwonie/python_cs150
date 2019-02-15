a = [0,1,2,[1,3,8,2],78,[5,3,9,4]]

# 1
for i in a : 
    if i % 2 == 0 :
        print(i)

#2
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

#3

count = 0
while count <= 10:
    if count == 2 or count == 5 or count == 7 :
        count +=1
        continue
    print(count)
    count += 1

#4
sum1 = []
sum2 = []
index1 = 3
index2 = 5
for index, item in enumerate(a) :
    if index == index1 :
        for element in item:
            sum1.append(element)
    elif index == index2 :
        for element in item:
            sum2.append(element)
        
print("sum1: {}".format(sum1))
print("sum2: {}".format(sum2))

