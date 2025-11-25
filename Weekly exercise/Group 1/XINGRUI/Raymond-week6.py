list = [3,7,2,9,4,1,8]
list.append(5)
list.remove(9)
list.sort() 
list.reverse()    
list.insert(2,6)
print(list.index(4))

my_tuple = (15,"Python",3.14,True,42,False)
print(my_tuple.index("Python"))
print(my_tuple.count(True))
print(my_tuple[1:5])

marks={"A":70,"B":71,"C":72,"D":73,"E":74,"F":75,"G":76,"H":77,"I":78,"J":79,"K":80,"L":81,"M":82,"N":83,"O":84}
marks["P"]=85
print(marks)