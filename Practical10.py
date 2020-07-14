x = int(input("Please enter age: "))

if x < 12 :
    print( 'You are a kid'  )
else :
    if x <18:
        print( 'You are young'  )
    else :
        print( 'You have grown up.'  )


#Ques-1:  9
#Ques-2: 15
#Ques-3: 25

#Second method

x = int(input("Please enter age: "))

if x < 12 :
    print( 'You are a kid'  )
elif x <18:
    print( 'You are young'  )
else :
    print( 'You have grown up.'  )
