numbers=[3,7,2,9,4,1,8]
numbers.append(5)
print(numbers)
numbers.remove(9)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.insert(2,6)
indexs=numbers.index(4)
print(indexs)


my_tuple=(15,"python",3.14,True,42,False)
print(my_tuple[1])
a=my_tuple.count(True)
print(a)
print(my_tuple[0:4])

student_marks={"A":85,"B":92,"C":78,"D":90,"E":88,"F":78,"G":90,"H":88,"I":92,"J":85}
student_marks["Frank"]=60
print(student_marks)