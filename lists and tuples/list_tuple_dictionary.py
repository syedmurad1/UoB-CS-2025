list = [1, 5, 7, 9, 3, 33] # List is mutable, ordered, allows duplicate members

tuple = (1, 5, 7, 9, 3, 33) # Tuple is immutable, ordered, allows duplicate members

print(tuple[2])

# set = {1, 5, 7, 9, 3, 33} # set is mutable, unordered, no duplicate members

# a dictionary is a collection of key-value pairs. Changeable and unordered. No duplicate members. {key1: value1, key2: value2}
dictionary_student = {"ID": "1", "name": "Tom","age": 22, "dep": "Computer Science"} 


print(dictionary_student)
# print(sdictionary_student["ID"])

staff = {"John":"manager",
         "Ali":"supervisor",
         "Tom":"CEO"}

print(staff)
print(staff.get("Tom"))

print(dir(staff))
print(help(staff))


# list[0]=10
# print(list)
# list.remove(3)
# print(list)
# print(len(list))
# print(33 in list)
# print(list.index(9))



capitals = {"UK": "London",
            "South Korea": "Seoul",
            "China": "Beijing",
            "Russia": "Moscow",
            "Japan": "Tokyo"
            }

print(dir(capitals))
print(help(capitals))
print(capitals.get("Japan"))
