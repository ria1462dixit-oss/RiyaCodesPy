choice = int(input("Enter problem number (1-25): "))

# Common inputs
n = int(input("Enter value of n: "))
num = int(input("Enter a number: "))
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

# Problem 1
if choice == 1:
    i = 1
    while i <= 10:
        print(i, end=" ")
        i += 1

# Problem 2
elif choice == 2:
    i = 1
    while i <= n:
        print(i, end=" ")
        i += 1

# Problem 3
elif choice == 3:
    i = 10
    while i >= 1:
        print(i, end=" ")
        i -= 1

# Problem 4
elif choice == 4:
    i = 1
    while i <= 10:
        print(i * 2, end=" ")
        i += 1

# Problem 5
elif choice == 5:
    i = 1
    while i <= 10:
        print(2 * i - 1, end=" ")
        i += 1

# Problem 6
elif choice == 6:
    i = 1
    while i <= n:
        print(i * 2, end=" ")
        i += 1

# Problem 7
elif choice == 7:
    i = 1
    while i <= n:
        print(2 * i - 1, end=" ")
        i += 1

# Problem 8
elif choice == 8:
    i = 1
    s = 0
    while i <= 10:
        s += i
        i += 1
    print(s)

# Problem 9
elif choice == 9:
    i = 1
    s = 0
    while i <= n:
        s += i
        i += 1
    print(s)

# Problem 10
elif choice == 10:
    i = 1
    while i <= 10:
        print("5 x", i, "=", 5 * i)
        i += 1

# Problem 11
elif choice == 11:
    i = 1
    while i <= 10:
        print(n, "x", i, "=", n * i)
        i += 1

# Problem 12
elif choice == 12:
    i = 1
    while i <= 100:
        print(i, end=" ")
        i += 1

# Problem 13
elif choice == 13:
    i = 1
    while i <= 50:
        if i % 5 == 0:
            print(i, end=" ")
        i += 1

# Problem 14
elif choice == 14:
    i = 1
    count = 0
    while i <= n:
        if i % 2 == 0:
            count += 1
        i += 1
    print(count)

# Problem 15
elif choice == 15:
    i = 1
    count = 0
    while i <= n:
        if i % 2 != 0:
            count += 1
        i += 1
    print(count)

# Problem 16
elif choice == 16:
    i = 1
    s = 0
    while i <= n:
        if i % 2 == 0:
            s += i
        i += 1
    print(s)

# Problem 17
elif choice == 17:
    i = 1
    s = 0
    while i <= n:
        if i % 2 != 0:
            s += i
        i += 1
    print(s)

# Problem 18
elif choice == 18:
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
    print(fact)

# Problem 19
elif choice == 19:
    i = 1
    while i <= 10:
        print(i * i, end=" ")
        i += 1

# Problem 20
elif choice == 20:
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    print(count)

# Problem 21
elif choice == 21:
    s = 0
    while num > 0:
        s += num % 10
        num = num // 10
    print(s)

# Problem 22
elif choice == 22:
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    print(rev)

# Problem 23 (Prime)
elif choice == 23:
    i = 2
    isPrime = 1

    if num <= 1:
        isPrime = 0
    else:
        while i <= num // 2:
            if num % i == 0:
                isPrime = 0
            i += 1

    if isPrime == 1:
        print("Prime")
    else:
        print("Not Prime")

# Problem 24
elif choice == 24:
    i = 1
    while i <= n:
        if i % 3 == 0:
            print(i, end=" ")
        i += 1

# Problem 25
elif choice == 25:
    result = 1
    i = 1
    while i <= exp:
        result *= base
        i += 1
    print(result)

else:
    print("Invalid choice")