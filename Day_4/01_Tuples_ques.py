# Tuples

# Q1. Access and unpack a tuple
# data = ("Garv", 22, "India")

# name, age, country=data 
# print(f"Name: {name} \n Age: {age} \n Country: {country}")



# Q2. Find the largest and smallest element
# Output:
# Largest = 23
# Smallest = 4
# Try solving it without directly using max() and min()
# elem= (15, 7, 23, 4, 18, 9)

# large= elem[0]
# small= elem[0]

# for i in elem:
#     if i>large:
#         large = i
#     if i<small:
#         small=i

# print(f"Largest = {large}")
# print(f"Smallest = {small}")



# Q3. Count an element
# Input: (1, 2, 3, 2, 4, 2, 5, 2)
# Element: 2

# Output:
# 2 occurs 4 times

# t= (1, 2, 3, 2, 4, 2, 5, 2)
# target=2
# count = 0

# for i in t:
#     if i == target:
#         count+=1
# print(f"{target} occurs {count} times")



# Q4. Convert between list and tuple
# numbers = [10, 20, 30, 40, 50]
# Convert it to a tuple, add 60 to the resulting data, and convert it back to a list.

# Expected:
# [10, 20, 30, 40, 50, 60]


# numbers = [10, 20, 30, 40, 50]
# # Convert list to tuple
# num_tuple= tuple(numbers)
# # Add 60 to the tuple (requires a trailing comma)
# num_tuple= num_tuple+(60,)
# # Convert back to a list
# final_list = list(num_tuple)

# print(final_list)



