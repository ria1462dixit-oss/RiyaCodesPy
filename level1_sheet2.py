# LEVEL 1 SHEET 2

# Problem 1 
print("\nProblem 1:")
num = int(input("Enter number: "))
if num >= 0:
    print("Positive")
else:
    print("Negative")


# Problem 2 
print("\nProblem 2:")
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Problem 3 
print("\nProblem 3:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greater:", a)
else:
    print("Greater:", b)


# Problem 4 
print("\nProblem 4:")
num = int(input("Enter number: "))
if num == 0:
    print("Zero")
else:
    print("Not Zero")


# Problem 5 
print("\nProblem 5:")
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")


# Problem 6 
print("\nProblem 6:")
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
else:
    print("Not Positive")


# Problem 7 
print("\nProblem 7:")
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")


# Problem 8 
print("\nProblem 8:")
num = int(input("Enter number: "))
if num % 5 == 0:
    print("Divisible")
else:
    print("Not Divisible")


# Problem 9 
print("\nProblem 9:")
num = int(input("Enter number: "))
if num % 10 == 0:
    print("Divisible")
else:
    print("Not Divisible")


# Problem 10 
print("\nProblem 10:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < b:
    print("Smaller:", a)
else:
    print("Smaller:", b)


# Problem 11 
print("\nProblem 11:")
num = int(input("Enter number: "))
if num >= 1 and num <= 10:
    print("Yes")
else:
    print("No")


# Problem 12 
print("\nProblem 12:")
num = int(input("Enter number: "))
if num % 3 == 0:
    print("Multiple of 3")
else:
    print("Not Multiple of 3")


# Problem 13 
print("\nProblem 13:")
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)


# Problem 14 
print("\nProblem 14:")
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a <= b and a <= c:
    print("Smallest:", a)
elif b <= a and b <= c:
    print("Smallest:", b)
else:
    print("Smallest:", c)


# Problem 15 
print("\nProblem 15:")
ch = input("Enter a character: ")

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else:
    print("Consonant")



# Problem 16 
print("\nProblem 16:")
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Grade F")


# Problem 17 
print("\nProblem 17:")
year = int(input("Enter year: "))
if year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")


# Problem 18 
print("\nProblem 18:")
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Problem 19 
print("\nProblem 19:")
num = int(input("Enter number: "))
if num >= 0 and num <= 9:
    print("Single Digit")
else:
    print("Not Single Digit")


# Problem 20 
print("\nProblem 20:")
units = int(input("Enter units: "))
if units <= 100:
    bill = units * 5
else:
    bill = units * 7
print("Total Bill:", bill)


# Problem 21 
print("\nProblem 21:")
a = int(input("Enter angle 1: "))
b = int(input("Enter angle 2: "))
c = int(input("Enter angle 3: "))

if a + b + c == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")


# Problem 22 
print("\nProblem 22:")
cp = float(input("Cost Price: "))
sp = float(input("Selling Price: "))

if sp > cp:
    print("Profit")
elif cp > sp:
    print("Loss")
else:
    print("No Profit No Loss")


# Problem 23 
print("\nProblem 23:")
num = int(input("Enter number: "))
if num % 2 == 0 and num % 3 == 0:
    print("Yes")
else:
    print("No")


# Problem 24 
print("\nProblem 24:")
temp = float(input("Enter temperature: "))

if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Normal")
else:
    print("Hot")


# Problem 25 
print("\nProblem 25:")
amount = float(input("Enter purchase amount: "))

if amount >= 1000:
    discount = amount * 0.10
    final = amount - discount
else:
    final = amount

print("Final Amount:", final)