#Given the following input  a = [ 7, 23, 56, 128, 92 48, 12, 32, 95 , 96 , 74, 93]

#1. multiply every fourth input in a. put the result in result1. Print out result1. 
# So result1 will have the product 128 * 32 * 93  

#2. multiply every third input in a (only if it is not the fourth input), put the result in result2. 
#Print out result2.  So result2  will have the product of 56x48x95

#3. add every second input in a (only if it is not the fourth or third input) put the result in result3.
#Print out result3.  So result3  will have the result 23 + 96

a = [ 7, 23, 56, 128, 92, 48, 12, 32, 95 , 96 , 74, 93]

result1 = 1
result2 = 1
result3 = 0

for index, i in enumerate(a):
    if index == 3 or index == 7 or index ==  11:
        result1 = result1 * i
        
    
    if index == 2 or index == 5 or index ==  8:
        result2 = result2 * i      
    
    if index == 1 or index == 9:
        result3 = result3 + i
        
print(result1)
print(result2)
print(result3)
