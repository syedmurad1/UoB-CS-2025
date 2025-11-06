# Initial list
numbers = [3, 7, 2, 9, 4, 1, 8]

# 1. Append the number 5
numbers.append(5)

# 2. Remove the number 9
numbers.remove(9)

# 3. Sort the list in ascending order
numbers.sort()

# 4. Reverse the list
numbers.reverse()

# 5. Insert the number 6 at index 2
numbers.insert(2, 6)

# 6. Print the index of the number 4
print(numbers.index(4))

my_tuple = (15, "Python", 3.14, True, 42, False)

# Print the index of the string "Python".
print(my_tuple.index("Python"))

# Count how many times the value True appears in the tuple.
count_true=my_tuple.count(True)

# Prints the elements from index 1 to index 4.
print(my_tuple[1:5])