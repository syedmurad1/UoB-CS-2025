### TASK 1
print("TASK 1:")
numbers = [3, 7, 2, 9, 4, 1]

numbers.append(5)
numbers.remove(9)


numbers.sort()
print(f"Sorted list: {numbers}")


numbers.sort(reverse=True)
print(f"Reveresed list: {numbers}")


numbers.insert(2, 6)
print(f"Number 6 was inserted: {numbers}")


print(f"The index of number 4 is: {numbers.index(4)}")



### TASK 2
print("TASK 2:")
my_tuple = (15, "Python", 3.14, True, 42, False)

print(f'Index of "Python is" {my_tuple.index("Python")}')

print(f"How many True values: {my_tuple.count(True)}")

for i in range(1, 5):
    print(my_tuple[i])
    i += 1



### TASK 3
print("TASK 3:")
students = {"name": ["Frank", "Tom"], "mark": [60, 65]}
print(students)

