# LEVEL1 SHEET 4 

#  Program 1: Extract Last Digit
print("\n  problem 1")
two_digit_num = int(input("Enter  a  two digit  number:"))
last_digit = two_digit_num % 10
print(f"Last digit of the number is : {last_digit}")

# Program 2: Remove Last Digit
print("\n  problem 2")
two_digit_num2 = int(input("Enter  a  two digit  number:"))
first_digit = two_digit_num2 // 10
print(f"the number after removing its last digit is : {first_digit}")

#  Program 3: Extract First Digit of 3-Digit Number 
print("\n  problem 3")
three_digit_num = int(input("Enter  a  three digit  number:"))
hundreds_digit = three_digit_num // 100
print(f"the first  digit  of the three digit number  is : {hundreds_digit}")

# Program 4: Extract Middle Digit of 3-Digit Number
print("\n  problem 4")
units_digit = three_digit_num % 10
remaining_two = three_digit_num % 100
tens_digit = remaining_two // 10
print(f"the middle  digit  of the three digit number  is : {tens_digit}")

# Program 5: Sum of Digits (3-digit number)
print("\n  problem 5")
digit_sum = hundreds_digit + tens_digit + units_digit
print(f"the first  digit  of the three digit number  is : {hundreds_digit}")
print(f"the middle  digit  of the three digit number  is : {tens_digit}")
print(f"the last  digit  of the three digit number  is : {units_digit}")
print(f"Sum of the three  digits of number {three_digit_num} is : {digit_sum}")

#  Program 6: Reverse a 2-Digit Number
print("\n  problem 6")
two_digit_num3 = int(input("Enter a two digit number:"))
tens_place = two_digit_num3 // 10
units_place = two_digit_num3 % 10
reversed_two_digit = (units_place * 10) + tens_place
print(f"The reversed number is : {reversed_two_digit}")

# Program 7: Reverse a 3-Digit Number
print("\n  problem 7")
reversed_three_digit = (units_digit * 100) + tens_digit * 10 + hundreds_digit
print(f"Reversed three digit number is :{reversed_three_digit}")

# Program 8: Swap First and Last Digit of 3-Digit Number
print("\n problem  8")
swapped_three_digit = (units_digit * 100) + tens_digit * 10 + hundreds_digit
print(f"After Swapping first digit with last digit:{swapped_three_digit}")

# Program 9: Average of First and Last Digit- 4digits
print("\n problem  9")
four_digit_num = int(input("Enter a  four digit number:"))
thousands_digit = four_digit_num // 1000

remaining_for_hundreds = four_digit_num % 1000
hundreds_digit4 = remaining_for_hundreds // 100

remaining_for_tens = four_digit_num % 100
tens_digit4 = remaining_for_tens // 10

print(thousands_digit)
print(hundreds_digit4)
print(tens_digit4)
units_digit4 = four_digit_num % 10
print(units_digit4)
avg = (thousands_digit + units_digit4) / 2
print(f"first digit is {thousands_digit}, last  digit is {units_digit4}. The average of  both the numbers is {avg}")

# Product of All Digits - 3  digits
print("\n problem 10")
digit_product = hundreds_digit * tens_digit * units_digit
print(f"Product of  the  digits in three digit number is : {digit_product}")

# Program 11: Check if Last Digit is Even
print("\n problem 11")
num11 = int(input("Enter a  number:"))
last_digit11 = num11 % 10
if last_digit11 % 2 == 0 : print("number is even")
else : print("number is odd")

# Program 12: Palindrome Number Checker (2-digit)
print("\n problem 12")
two_digit_num4 = int(input("Enter a two digit number:"))
first_digit12 = two_digit_num4 // 10
last_digit12 = two_digit_num4 % 10
if first_digit12 == last_digit12 : print("It is a pallindrome  number")
else:  print("Not a pallindrome number")

# Program 13: Palindrome Number Checker (3-digit)
print("\n problem 13")
if three_digit_num == reversed_three_digit: print("It is a pallindrome  number as the  number  you  entered  is {three_digit_num} and  it does not match with the reversed form {reversed_three_digit}")
else:  print(f"Not a pallindrome number as the  number  you  entered  is {three_digit_num} and  it does not match with the reversed form {reversed_three_digit}")

# Program 14: Find Largest Digit in a Number
print("\n problem 14")

largest_digit = thousands_digit

if hundreds_digit4 > largest_digit:
    largest_digit = hundreds_digit4

if tens_digit4 > largest_digit:
    largest_digit = tens_digit4

if units_digit4 > largest_digit:
    largest_digit = units_digit4

print("Largest digit is:", largest_digit)

# Program 15: Find Smallest Digit in a Number
print("\n problem 15")

smallest_digit = thousands_digit

if hundreds_digit4 < largest_digit:
    largest_digit = hundreds_digit4

if tens_digit4 < largest_digit:
    largest_digit = tens_digit4

if units_digit4 < largest_digit:
    largest_digit = units_digit4

print("smallest digit is:", smallest_digit)

# 16: Check Divisibility by 3 Using Digit Sum
print("\n problem 16")

digit_sum4 = thousands_digit + hundreds_digit4 + tens_digit4 + units_digit4

print("Sum of digits:", digit_sum4)

if digit_sum4 % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")

 # Program 17: Count Even Digits in a Number
print("\n problem 17")
even_count = 0

if thousands_digit % 2 == 0:
  even_count = even_count + 1

if hundreds_digit4 % 2 == 0:
  even_count = even_count + 1

if tens_digit4 % 2 == 0:
 even_count = even_count + 1

if units_digit4 % 2 == 0:
  even_count = even_count + 1

print(f"Number of even digits in this {four_digit_num} number  is : {even_count}")

# Program 18: Check if Digits are in Ascending Order
print("\n problem 18")
if hundreds_digit < tens_digit < units_digit : print(f"Yes! The number {three_digit_num} is in asecending order")

# Program 19: Harshad/Niven Number Checker (3-digit)
print("\n problem 19")
harshad_result = three_digit_num / digit_sum
if harshad_result % digit_sum == 0 : print("Harshad number")
else : print ("It is not a harshad number")

# Program 20: Duck Number Checker (4-digit)
print("\n  problem 20")
if thousands_digit == 0 : print("Not a duck number")
if hundreds_digit4 == 0 or tens_digit4 == 0 or units_digit4 : print("It is a  duck number")