# Sets

# Q1. Remove duplicates
# Input: [1, 2, 2, 3, 4, 4, 5, 5, 5]
# Output: {1, 2, 3, 4, 5}

# a=[1, 2, 2, 3, 4, 4, 5, 5, 5]
# set_list= set(a)
# print(set_list)


# Q2. Set operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# Find:  Union| Intersection| Elements only in A| Elements only in B

# print(A | B)  # union

# print(A & B)  #Intersection

# print(A-B)      # Elements only in A

# print(B-A)       # Elements only in B



# Q3. Find common elements
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

# Output:
# Common elements: {30, 40, 50}

# lis1= set(list1)
# lis2 = set(list2)

# print(lis1 & lis2 )




# Q8. Check subset
A = {1, 2, 3, 4, 5}
B = {2, 3, 4}

# Check whether B is a subset of A.
# Expected:
# B is a subset of A

# if B <= A:
#     print("B is a subset of A")
# else:
#     print("B is not a subset of A")