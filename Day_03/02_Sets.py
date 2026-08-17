a={}  # if u will not enter anything in it it will not be considerd as  tuple
print(type(a))   #dict 

# Sets contains only unique value




#Methods:
# l={10,20,30,40}

# l.add(50)
# print(l)

# # l.clear()       # clear all values from sets

# l.discard()    # Remove the specfied elem

# l.pop()   # remove random value





# Set Operations
s1={10,20,30,40}
s2={30,40,50,60}

print(s1.difference(s2))     # also write s1-s2

# s2-=s1
# print(s2)        # that diffrence value will be going to assign in the s2 var

print(s1.intersection(s2))  # or also u can use (s1 & s2)


s3={30,40}

print(s3.issubset(s2))
print(s3<=s2)     


print(s2.issuperset(s3))
print(s2>=s3)              # means s2 values only shoul include in s3

print(s1.symmetric_difference(s2))   # only wants diffrents sets values
print(s1^s2)

print(s2.union(s1))   # return all values in one set
print(s1 | s2)