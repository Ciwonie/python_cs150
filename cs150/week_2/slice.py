print("Hello World!")

## EXMAPLE 1
a = [3, 5, 7, 28, 4, 9, 10]
print(a[:3])
print(a[2:])
print(a[2:5])

## EXMAPLE 2
b = [20, 12, [3, [45, 6], 10], 4]
print(b[2])
print(b[2][1])

## EXAMPLE 3


while True:
  try:
    hours = float(input("Enter hours worked: "))  
    hourly_pay = float(input("Enter hourly pay: "))
  except ValueError:
     print("Please input a number: ")
     continue
  else:
     break 

over_hours = hours - 40

if over_hours > 0 :
    over_pay = 0.5 * over_hours * hourly_pay
else :
    over_pay = 0

salary = hours * hourly_pay + over_pay

if salary > 2000 :
    tax_rate = 0.25
elif salary > 1500 :
    tax_rate = 0.2
elif salary > 1000 :
	tax_rate = 0.15
elif salary > 500 :
	tax_rate = 0.1
else :
	tax_rate = 0

tax = tax_rate * salary
net = salary - tax

print("We took out ${} in taxes.".format(tax))
print("Your pay before taxes is ${}.".format(salary))
print("Your take-home pay is ${}.".format(net))
print("Have a nice life.")

