#RULE-1: Lists are mutable= modification allowed
#----------------------------
a = ["Noida", "Delhi", "Lucknow", "Goa", "Kanpur"] # This is list
#      0         1        2         3       4

print( a  )
a[3] = "UK"
print( a  )

a.append("Patna")
print( a  )

del a[1]
print( a )

a.insert(1, "Varanasi")
print( a )
