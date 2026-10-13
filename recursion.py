# Print numbers from 1 to n

def count(n): 
    if n == 0: 
        return 

    count(n - 1)
    print(n)

num1 = int(input("Enter a number: "))
count(num1)

# Print numbers from n to 1

def countdown(n): 
    if n == 0: 
        return

    print(n)
    countdown(n - 1)

num2 = int(input("Enter a number: "))
countdown(num2)

# Calculate the factorial of a number 

def factorial(n): 
    if n == 0 or n == 1: 
        return 1

    return n * factorial(n - 1)

num3 = int(input("Enter a number: "))
result = factorial(num3)

print("Factorial = ", result)

# Calculate the power of a number 

def power(base, exponent): 
    if exponent == 0: 
        return 1

    return base * power(base, exponent - 1)

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

if exponent < 0: 
    print("Please enter a non-negative exponent.")

else: 
    result = power(base, exponent)
    print("Result =", result)