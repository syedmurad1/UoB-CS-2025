#The following a list of integers: numbers=[3,7,2,9,4,1,8]
tmpList=[3,7,2,9,4,1,8]

#Append the number 5 to the list.
tmpList.append(5)

#Remove the number 9 from the list.
tmpList.remove(9)

#Sort the list in ascending order.
tmpList.sort()

#Reverse the list after sorting it.
tmpList.reverse()

#Insert the number 6 at the index 2.
tmpList.insert(2,6)

#Print the index of the number 4 in the list.
print(tmpList.index(4))

#The following tuple of mixed data types: my_tuple=(15,"Pyrhon",3.14,True,42,False)
my_tuple=(15, "Python", 3.14, True, 42, False)

#Print the index of the string "Python".
print(my_tuple[1])

#Count how many times the value True appears in the tuple.
print(my_tuple.count(True))

#Print the elements from index 1 to index 4.
print(my_tuple[1:5])

#Create a python dictionary representing the marks of students (at least 15 students) in a test.
students={"Mikel":80,
          "Tim":80,
          "Muhammad":15,
          "Noah":50,
          "Oliver":35,
          "Arthur":75,
          "Leo":25,
          "George":90,
          "Luca":40,
          "Theodore":55,
          "Oscar":45,
          "Archie":60,
          "Olivia":95,
          "Amelia":85,
          "Lily":30
          }

#Add a new student "Frank" with a mark of 60.
students["Frank"]=60

#Print all student names and their corresponding marks.
print(students)