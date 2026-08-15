# Check whether a number is positive, negative, or zero.
a=0
if a>0:
    print("Positive number")
elif a<0:
    print("Negative Number")
else:
    print("Zero number")


# Check whether a number is even or odd.
b=6
if a%2==0:
    print(f"{b} is a even number")
else:
    print(f"{b} is a odd number")


# Find the greater of two numbers.
a = 15
b = 27
if a > b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")


# Check whether someone is eligible to vote.
c=input("Enter your age to check eligiblity: ")

if c>=18:
    print(f"{c} is eligible")
else:
    print(f"{c} is not eligible")

# Calculate grade from marks.
d=input("Enter your marks to check grades:")

if d>=80:
    print("A+")
elif d>=70:
    print("A")
elif d>=60:
    print("B")
elif d>=40:
    print("C")
else:
    print("F")


# Check whether a year is a leap year.
y = 1900

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("Leap year") 
else:
    print("Not a leap year")

# Find the greatest of three numbers.
a1=20
a2=30
a3=40

if (a1>=a2 and a1>=a3):
    print("A1 is greater")
elif (a2>=a1 and a2>=a3):
    print("A2 is greater")
else:
    print("A3 is greater")



# Build a simple calculator using if-elif-else
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Error: Invalid operator. Please use +, -, *, or /.")
