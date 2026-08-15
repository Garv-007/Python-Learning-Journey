# Ranges
# for i in range(10,101):
#     print(i)



# Q1: Print "Hello World" n times.
# n=int(input("How many times u want me to print Hello World: "))

# for i in range(1,n+1):
#     print("Hello World")


# Q2: Print natural numbers from 1 to n.
# n=int(input("Enter number:"))
# for i in range(1,n+1):
#     print(i)

# Q3: Reverse for loop — print n down to 1.
# n=int(input("Enter number:"))
# for i in range(n,0,-1):
#     print(i)

# Q4: Print the multiplication table of a number.
# n=int(input("Enter number:"))
# for i in range(1,11):
#     print(f"{n}X{i}={n*i}")

# Q5: Sum of first n natural numbers.
# n= int(input("Enter your number:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# Q6: Factorial of a number.
# n= int(input("Enter your number:"))
# fact=1
# for i in range(1,n+1):
#     fact = fact *i
# print(fact)

# Q7: Print sum of all even and odd numbers in a range separately.
# n= int(input("Enter your number:"))
# even_sum=0
# odd_sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         even_sum = even_sum+i
#     else:
#         odd_sum=odd_sum+i
# print(f"Even Sum= {even_sum}, Odd Sum={odd_sum}")
    

# Q8: Print all factors of a number.
# n= int(input("Enter your number:"))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# Q9: Check if a number is perfect (sum of factors = the number itself).
# n= int(input("Enter your number:"))
# sum=0

# for i in range(1,n):
#      if n%i==0:
#         sum= sum+i
# if sum==n:
#     print("PERFECT NUMBER")
# else:
#     print("Not A perfect Number")


# Q10: Check if a number is prime.
# n= int(input("Enter your number:"))
# count =0
# for i in range(1,n+1):
#     if n%i==0:
#         count =count+1
# if count==2:
#     print("Prime number")
# else:
#     print("Not A Prime Number")


# Q11: Reverse a string without using built-in functions.

# a= "python"
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev= rev+ a[i]

# print(rev)


# Q12: Check if a string is a palindrome.
# a= "naman"
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev= rev+ a[i]

# if rev==a:
#     print("This Palandrome Number")
# else:
#     print("Not A Palandrome Number")


# Q13: Count letters, digits, and special symbols in a string.
a= "P@#yn26at^&i5ve"

#Using Built in Functions

# char= 0
# spchar=0
# digits=0

# for i in a:
#     if i.isdigit():
#         digits=digits+1
#     elif i.isalpha():
#         char=char+1
#     else:
#         spchar=spchar+1
# print(f"{char} is char ,{digits} is digits , {spchar} is char")


char= 0
spchar=0
digits=0

for i in a:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        char=char+1
    elif ord(i)>=48 and ord(i)<=90:
        digits=digits+1
    else:
        spchar=spchar+1
print(f"{char} is char ,{digits} is digits , {spchar} is char")