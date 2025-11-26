a = [3, 7, 2, 9, 4, 1, 8]

# Append the number 5 to the list
a.append(5)
print(a)

# Remove the number 9 from the list
a.remove(9)
print(a)

# Sort the list in ascending order
a.sort()
print(a)

# Reverse the list after sorting it
a.reverse()
print(a)

# Insert the number 6 at the index 2
a.insert(2, 6)
print(a)

# Print the index of the number 4 in the list
print(a.index(4))


b = (15, "Python", 3.14, True, 42, False)

# Print the index of the string "Python"
print(b.index("Python"))

# Count how many times the value True appears in the tuple
x = b.count(True)
print(x)

# Print the elements from index 1 to 4
print(b[1:5])

student_marks = {"Miller": 90, "Adams": 75, "Tom": 84, "Liam": 96, "David": 67, "Jack": 77, "Noah": 54, "Lucas": 100, "Chloe": 82, "Thomas": 89, "William": 80, "Ethan": 72, "Jackson": 95, "Paul": 64, "Karen": 88}

# Add a new student "Frank" with a mark of 60
student_marks.update({"Frank": 60})
print(student_marks)
