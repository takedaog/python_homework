#1. Check if username and password are not empty

username = input("Username: ")
password = input("Password: ")
print("Valid input:", bool(username) and bool(password))

#2. Check if two numbers are equal

a = int(input("First number: "))
b = int(input("Second number: "))
if a == b:
    print("Numbers are equal")
else:
    print("Not equal")

#3. Check if number is positive and even

num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("Positive and even")
else:
    print("Not positive and even")

#4. Check if three numbers are all different

a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))
if a != b and b != c and a != c:
    print("All numbers are different")
else:
    print("Some numbers are the same")

#5. Check if two strings have same length

a = input("First string: ")
b = input("Second string: ")
print("Same length:", len(a) == len(b))
#6. Check if divisible by 3 and 5

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

#7. Check if sum of two numbers > 50

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a + b > 50:
    print("Sum is greater than 50")
else:
    print("Sum is 50 or less")

#8. Check if number is between 10 and 20

num = int(input("Enter a number: "))
if 10 <= num <= 20:
    print("Number is between 10 and 20")
else:
    print("Not in range")