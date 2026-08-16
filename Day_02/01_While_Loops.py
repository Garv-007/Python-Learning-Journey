# a=1

# while a<=20:
#     print(a)
#     a=a+1


# Q1: Separate each digit of a number and print on a new line
# a= 12345

# while a>0:
#     print(a%10)
#     a=a//10


# Q2: Accept a number and print its reverse.
# b= int(input("Enter your number:"))
# rev=0
# # rev=rev*10 + b%10
# while b>0:
#       rev =rev *10 + b%10
#       b=b//10
# print(rev)


# Q3: Check if a number is palindromic (equal to its reverse).
b= int(input("Enter your number:"))
copy=b
rev=0
# rev=rev*10 + b%10
while b>0:
      rev =rev *10 + b%10
      b=b//10
if rev==copy:
      print("this is palandrome number")
else:
      print("this is not a palandrome number")