# Dictionaries questions


# Q1. Student information
# Create a dictionary:
student = {
    "name": "Garv",
    "age": 22,
    "course": "BCA",
    "marks": 85
}

# Print each piece of information in this format:
# Name: Garv Age: 22  Course: BCA  Marks: 85

# for i in student:
#     print(f"{i}:{student[i]}")



# Q10. Find the student with the highest marks
students = {
    "Rahul": 78,
    "Aman": 92,
    "Priya": 85,
    "Neha": 88
}
# Output:
# Top student: Aman
# Marks: 92
# Try doing it without max().



# top_student = None
# highest_marks = -1

# for name, marks in students.items():
#     if marks > highest_marks:
#         highest_marks = marks
#         top_student = name

# print(f"Top student: {top_student}")
# print(f"Marks: {highest_marks}")



# Q11. Count frequency of characters
text = "programming"
# Create a dictionary containing the frequency of every character.

frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)