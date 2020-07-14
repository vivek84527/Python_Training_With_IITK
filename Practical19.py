arr=['Mary', 'had', 'a', 'little', 'lamb']

print( list( enumerate(arr) )  )
print( tuple( enumerate(arr) )  )


for i , j in list( enumerate(arr) ) :
    print( i , " = " , j   )

for i  in list( enumerate(arr) ) :
    print( i , type(i) )
