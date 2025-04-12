# 1. Round float to 2 decimal places

num = float(input("Enter a float number: "))
print("Rounded:", round(num, 2))

# 2. Largest and smallest of three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print("Largest:", max(a, b, c))
print("Smallest:", min(a, b, c))


# 3. Kilometers to meters and centimeters

km = float(input("Enter distance in kilometers: "))
meters = km * 1000
centimeters = km * 100000
print("Meters:", meters)
print("Centimeters:", centimeters)

# 4. Integer division and remainder

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Integer division:", a // b)
print("Remainder:", a % b)


# 5. Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)

# 6. Return last digit

num = int(input("Enter a number: "))
print("Last digit:", abs(num) % 10)

# 7. Check if even

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

