# Output — print()
name = "Akarsh"
age  = 20

print("Hello!")                         # basic
print(f"My name is {name}")              # f-string
print("Name:", name, "Age:", age)      # multiple values


# Input — input()
# Remember:
# input() always returns a
# string
# . If you need a number, convert it manually with int() or float().

name = input("What is your name? ")
age  = int(input("How old are you? "))

print(f"Hello {name}, you are {age} years old!")
