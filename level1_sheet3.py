# LEVEL1 SHEET 3

# Problem 1 
print("\nProblem 1: Positive / Negative / Zero")
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Problem 2 
print("\nProblem 2: Even or Odd")
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Problem 4 
print("\nProblem 4: Divisibility Check")
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
if a % b == 0:
    print("Divisible")
else:
    print("Not Divisible")


# Problem 5 
print("\nProblem 5: Vowel or Consonant")
ch = input("Enter character: ")
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print("Vowel")
else:
    print("Consonant")


# Problem 6 
print("\nProblem 6: Alphabet / Digit / Special")
ch = input("Enter character: ")
if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
    print("Alphabet")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special Character")


# Problem 7 
print("\nProblem 7: Uppercase or Lowercase")
ch = input("Enter alphabet: ")
if ch >= 'A' and ch <= 'Z':
    print("Uppercase")
else:
    print("Lowercase")


# Problem 9 
print("\nProblem 9: Voting Eligibility")
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# Problem 13 
print("\nProblem 13: Greatest of Three")
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)


# Problem 15 
print("\nProblem 15: Digit Category")
num = int(input("Enter number: "))
if num >= 0 and num <= 9:
    print("Single Digit")
elif num >= 10 and num <= 99:
    print("Double Digit")
else:
    print("More than Double Digit")


# Problem 16 
print("\nProblem 16: Grade Calculator")
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
elif marks >= 40:
    print("E")
else:
    print("F")


# Problem 17 
print("\nProblem 17: Triangle Type (Sides)")
a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

if a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


# Problem 18 
print("\nProblem 18: Triangle Validity (Sides)")
a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

if a + b > c and b + c > a and a + c > b:
    print("Valid")
else:
    print("Invalid")


# Problem 19 
print("\nProblem 19: Quadrant Finder")
x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
elif x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("Y-axis")
else:
    print("X-axis")


# Problem 20 
print("\nProblem 20: BMI Category")
bmi = float(input("Enter BMI: "))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


# Problem 21 
print("\nProblem 21: Day of Week")
day = int(input("Enter number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid")


# Problem 22 
print("\nProblem 22: Month Days")
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

if month == 2:
    if year % 4 == 0:
        print("29 days")
    else:
        print("28 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
elif month >= 1 and month <= 12:
    print("31 days")
else:
    print("Invalid month")


# Problem 25 
print("\nProblem 25: Number Range")
num = int(input("Enter number: "))

if num <= 10:
    print("1-10")
elif num <= 50:
    print("11-50")
elif num <= 100:
    print("51-100")
elif num <= 500:
    print("101-500")
elif num <= 1000:
    print("501-1000")
else:
    print("Above 1000")


# Problem 28 
print("\nProblem 28: Divisible by 3 and 5")
num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by Both")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible")


# Problem 27 
print("\nProblem 27: Electricity Bill")
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
elif units <= 300:
    bill = units * 10
else:
    bill = units * 15

print("Bill:", bill)


# Problem 32 
print("\nProblem 32: Income Tax")
income = float(input("Enter income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Tax:", tax)


# Problem 33 
print("\nProblem 33: Ticket Price")
age = int(input("Enter age: "))

if age <= 12:
    print("100")
elif age <= 17:
    print("150")
elif age <= 59:
    print("200")
else:
    print("120")


# Problem 34 
print("\nProblem 34: Salary Increment")
salary = float(input("Enter salary: "))
rating = int(input("Enter rating (1-5): "))
years = int(input("Years of service: "))

if rating == 5:
    inc = 0.20
elif rating == 4:
    inc = 0.15
elif rating == 3:
    inc = 0.10
elif rating == 2:
    inc = 0.05
else:
    inc = 0

if years > 5:
    inc = inc + 0.05

new_salary = salary + (salary * inc)
print("New Salary:", new_salary)


# ------------------ Problem 35 ------------------
print("\nProblem 35: Loan Eligibility")
age = int(input("Age: "))
income = float(input("Income: "))
credit = int(input("Credit Score: "))

if age >= 21 and age <= 60 and income > 25000 and credit > 700:
    print("Eligible")
else:
    print("Not Eligible")


# ------------------ Problem 36 ------------------
print("\nProblem 36: Password Strength")
length = int(input("Length: "))
upper = int(input("Uppercase count: "))
lower = int(input("Lowercase count: "))
digit = int(input("Digit count: "))

if length >= 8 and upper > 0 and lower > 0 and digit > 0:
    print("Strong")
elif length >= 6 and ((upper > 0 and lower > 0) or (upper > 0 and digit > 0) or (lower > 0 and digit > 0)):
    print("Medium")
else:
    print("Weak")


# ------------------ Problem 37 ------------------
print("\nProblem 37: Admission Eligibility")
m = int(input("Maths: "))
p = int(input("Physics: "))
c = int(input("Chemistry: "))

total = m + p + c

if m >= 80 and p >= 75 and c >= 75 and total >= 240:
    print("Eligible")
else:
    print("Not Eligible")



# Problem 38 
print("\nProblem 38: Discount System")
amount = float(input("Enter amount: "))
member = int(input("Member? (1 yes / 0 no): "))

if amount > 10000:
    disc = 0.20
elif amount > 5000:
    disc = 0.15
elif amount > 2000:
    disc = 0.10
else:
    disc = 0

if member == 1:
    disc = disc + 0.05

final = amount - (amount * disc)
print("Final Price:", final)


# Problem 39 
print("\nProblem 39: Shipping Cost")
weight = float(input("Weight: "))
distance = float(input("Distance: "))

cost = 50

if weight > 5:
    cost = cost + (weight * 10)

if distance > 100:
    cost = cost + (distance * 5)

if weight > 5 and distance > 100:
    cost = cost + 20

print("Shipping Cost:", cost)


# Problem 40 
print("\nProblem 40: Water Bill")
usage = float(input("Water usage (L): "))

if usage <= 5000:
    bill = usage * 2
elif usage <= 10000:
    bill = usage * 3
else:
    bill = usage * 5

if usage < 3000:
    bill = bill - (bill * 0.15)

print("Water Bill:", bill)