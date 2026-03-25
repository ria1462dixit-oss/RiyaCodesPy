# LEVEL1 SHEET 1 

#  Problem 1 
print("\nProblem 1:")
num = 10
print("Initial:", num)

num = 20
print("Updated to 20:", num)

num = num + 5
print("After adding 5:", num)

num = num * 2
print("After multiplying by 2:", num)


# Problem 2 
print("\nProblem 2:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)


#  Problem 3
print("\nProblem 3:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# Problem 4 
print("\nProblem 4:")
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
sum_val = a + b + c
print("Sum:", sum_val)
print("Average:", sum_val / 3)


# Problem 5 
print("\nProblem 5:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swap:", a, b)
temp = a
a = b
b = temp
print("After swap:", a, b)


# Problem 6 
print("\nProblem 6:")
m1 = int(input("Marks 1: "))
m2 = int(input("Marks 2: "))
m3 = int(input("Marks 3: "))
total = m1 + m2 + m3
print("Total:", total)
print("Percentage:", total / 3)


# Problem 7 
print("\nProblem 7:")
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
si = (p * r * t) / 100
print("Simple Interest:", si)


# Problem 8 
print("\nProblem 8:")
c = float(input("Enter Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit:", f)


# Problem 9 
print("\nProblem 9:")
f = float(input("Enter Fahrenheit: "))
c = (f - 32) * 5/9
print("Celsius:", c)


# Problem 10 
print("\nProblem 10:")
l = float(input("Length: "))
w = float(input("Width: "))
print("Area of Rectangle:", l * w)


# Problem 11 
print("\nProblem 11:")
r = float(input("Radius: "))
area = 3.14159 * r * r
print("Area of Circle:", area)


# Problem 12 
print("\nProblem 12:")
b = float(input("Base: "))
h = float(input("Height: "))
print("Area of Triangle:", (b * h) / 2)


# Problem 13 
print("\nProblem 13:")
s = float(input("Side: "))
print("Area:", s * s)
print("Perimeter:", 4 * s)


# Problem 14 
print("\nProblem 14:")
l = float(input("Length: "))
w = float(input("Width: "))
print("Area:", l * w)
print("Perimeter:", 2 * (l + w))


# Problem 15 
print("\nProblem 15:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swap:", a, b)

a = a + b
b = a - b
a = a - b

print("After swap:", a, b)


# Problem 16 
print("\nProblem 16:")
days = int(input("Enter total days: "))
years = days // 365
days = days % 365
weeks = days // 7
days = days % 7
print("Years:", years)
print("Weeks:", weeks)
print("Days:", days)


# Problem 17 
print("\nProblem 17:")
sec = int(input("Enter seconds: "))
hours = sec // 3600
sec = sec % 3600
minutes = sec // 60
seconds = sec % 60
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)


# Problem 18 
print("\nProblem 18:")
m1 = int(input("Marks 1: "))
m2 = int(input("Marks 2: "))
m3 = int(input("Marks 3: "))
m4 = int(input("Marks 4: "))
m5 = int(input("Marks 5: "))
total = m1 + m2 + m3 + m4 + m5
print("Total:", total)
print("Average:", total / 5)


# Problem 19 
print("\nProblem 19:")
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
si = (p * r * t) / 100
print("Simple Interest:", si)
print("Total Amount:", p + si)


# Problem 20 
print("\nProblem 20:")
cp = float(input("Cost Price: "))
sp = float(input("Selling Price: "))

if sp > cp:
    print("Profit:", sp - cp)
elif cp > sp:
    print("Loss:", cp - sp)
else:
    print("No Profit No Loss")


# Problem 21 
print("\nProblem 21:")
price = float(input("Original Price: "))
discount = float(input("Discount %: "))
final_price = price - (price * discount / 100)
print("Final Price:", final_price)


# Problem 22 
print("\nProblem 22:")
price = float(input("Price: "))
qty = int(input("Quantity: "))
tax = float(input("Tax %: "))

subtotal = price * qty
tax_amt = subtotal * tax / 100
total = subtotal + tax_amt

print("Subtotal:", subtotal)
print("Tax:", tax_amt)
print("Total:", total)


# Problem 23 
print("\nProblem 23:")
units = float(input("Units Consumed: "))
rate = float(input("Rate per unit: "))
bill = units * rate
print("Total Bill:", bill)


# Problem 24 
print("\nProblem 24:")
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = weight / (height * height)
print("BMI:", bmi)