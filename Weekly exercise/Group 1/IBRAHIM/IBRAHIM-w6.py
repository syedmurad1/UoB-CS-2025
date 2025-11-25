student_marks = {
    "s1": 85,
    "s2": 90,
    "s3": 78,
    "s4": 92,
    "s5": 88,
    "s6": 76,
    "s7": 95,
    "s8": 81,
    "s9": 89,
    "s10": 93,
    "s11": 77,
    "s12": 84,
    "s13": 91,
    "s14": 80,
    "Frank": 87  # The 15th student
}
 
# 2. Print Frank's name and his mark
print(f"Frank: {student_marks['Frank']}")
 
 
list22 = [ 10, 20, 30,40,50]
list22.reverse()
print(list22)
 
print(list22.index(20))
index = list22.index(20)
list22[index] = 200
print(list22)
index2 = list22.index(10)
list22[index2] = 50
print(list22)
name = input("please enter first name")
print(name)
 
 
 
list1 = [3,7,2,9,4,1,8]
list1.append(5)
index = index = list1.index(2)
list1[index] = 6
list1.remove(4)
list1.sort()
# print(list1)
list1.reverse()
print(list1.index(4))
 
my_tuple = (15 , "python", 3.14,True , 42 , False)
print(my_tuple.index("python"))
amount = my_tuple.count(True)
print(amount)
print(my_tuple[1:4])