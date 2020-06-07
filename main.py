



















"""x=1
y=1
o=0

n =int(input("how many terms"))
if n<0: 
    print("Incorrect input")
elif n==1: 
    print (o) 
    
elif n==2: 
    print (1)
else: 
  while True:
    
    o + y == x """

  















#pascal's triangle 
"""x = int(input("how many lines of pascal's triangle"))
a = '*' 
b = " "
for i in range(0,x):
  for j in range(0,x):
    print (end = b)
  x = x - 1 
  for j in range (0,i + 1):
      print (a, end = b)
  print ("\r")
#whether a prime number or not quit at 0

while True:
  x = int(input("enter a number"))
 
  if x == 0:
    break
  elif x == 2 or x == 3 or x == 5 or x == 7 :
    print ("true")
  elif x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 9 == 0 :
    print ("false")
  else:
    print ("true")
  
#show first n prime numbers 
x = int(input("how many prime numbers"))

y = []

j = 1

flag = True
while flag:
  j = j + 1
  if j == 2 or j == 3 or j == 5 or j == 7 :
    y.append(j)
    print (j)
  elif j % 2 == 0 or j % 3 == 0 or j % 5 == 0 or j % 7 == 0:
    pass
  else:
    y.append(j)
    print (j)
  if len(y) == x:
    
    break
  else:
    continue
"""






#Fizz buzz
"""while True:
  x = int(input("Enter a number: "))
  if x%3 == 0 and x%5 ==0:
    print ("FIZZ BUZZ")
  elif x%3 == 0:
    print ("FIZZ")
  elif x%5 == 0:
    print ("BUZZ")
  elif x == -1:
    break
  else:
    print ("OOPS")
fan_status = "on"
while True:
  command = input("enter a command (on,off, or quit)")
  command = command.lower()
  if command == "on":
    if fan_status == "on":
      print ("fan already on")
    else:
      print ("fan turned on")
      fan_status = "on"
  elif command == "off":
    if fan_status == "off":
      print ("fan already off")
    else:
      print ("fan turned off")
      fan_status = "off"
  elif command == "quit":
    break
  else:
    print ("invalid syntax")


# day 1



print ("45 * 45 = " + str(45 * 45))

print ("it")
# day 2 
print ("-----" * 3)


a = int(input("enter a number "))
b = int (input("enter a number"))
print (f"the sum of {a} + {b} = {a + b}")


print ("---" * 3)
#day2 project
first_name=input('Enter your firstname')
last_name=input('Enter your last name')
address=input('Enter your address')
zipcode=input('Enter your zipcode')
birth_year= int (input('Enter your year of birth'))
hi = 2020
age = hi - birth_year
print(f'''Name: {first_name} {last_name}
Address: {address}
Zip: {zipcode}
Age: {age}''')
print ("---" * 3)
#python operations
number1 = int(input("Enter number1 "))
number2 = int(input("Enter number2 "))

print(f'Result of {number1} + {number2} = {number1 + number2}')
print(f'Result of {number1} - {number2} = {number1 - number2}')
print(f'Result of {number1} * {number2} = {number1 * number2}')
print(f'Result of {number1} / {number2} = {number1 / number2}')

# % means modulus (Reminder)
print(f'Result of {number1} % {number2} = {number1 % number2}')

# ** means Exponent
print(f'Result of {number1} ** {number2} = {number1 ** number2}')

# // means floor division
print(f'Result of {number1} // {number2} = {number1 // number2}')
print ("---" * 3)
#string methods (homework day2)
string = "My NaMe IS bob"
x = string.swapcase()
print (x)
string = "HELLO!"
x = string.casefold()
print(x)
string = "I like mangoes"
x = string.replace("mangoes", "fruit")
print(x)
string = "bob"
x = string.center(30)
print(x)
string = "Hello, welcome"
x = string.endswith("come")
print(x)
print ("---" * 3)
#day3
x = int(input ("enter x"))
y = int(input("enter y"))
if x > y:
  print (f"x-y = {x-y}")
elif x < y:
  print (f"y-x = {y-x}")
else:
  print ("x and y are equal")
# project 2
child_age = int(input("enter your child's age"))

if 4 < child_age > 0:
  print ("your child is a toddler")
elif 13 < child_age > 3:
  print ("your child is a kid") 
elif 19 < child_age > 12:
  print ("your child is a teen")
else:
  print ("your child is an adult")
#project3
x = int(input("enter you're weight"))
y = input("is it pounds(p) or kg")
if y.lower() == "kg":
  print (f"you're weight in pounds is {x * 2.2}")
elif y.lower == "p":
  print (f"you're weight in kg is {x / 2.2}")


for x in range(10,20,10):
  print (x)


#get an input print whether a number is even or odd
x = int(input("Enter a number to validate even or odd: "))
if (x%2)==0:
  print (f"{x} is an even number")
else:
  print (f"{x} is an odd number")
#print whether a number is divisble by 5
y = int(input("Enter a number to validate divisible by 5: "))
if (y%5)==0:
  print (f"{y} is divisble by 5")
else:
  print (f"{y} is not divisible by 5")
#factorial of n 
x = int (input("enter a number:"))
factorial = 1
for y in range(2, x + 1):
  factorial *= y
print (f"factorial of {x} is {factorial}")"""
#on fan turn on off turn off until quit




