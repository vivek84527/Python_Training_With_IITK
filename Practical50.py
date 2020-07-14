s1 = "python is simple."
s2 = s1.capitalize()
print (s2)
#Python is simple.


s1 = "3 is greater than 2."
s2 = s1.capitalize()
print (s1)
#3 is greater than 2.

s1 = "india"
s2 = s1.center(20)
print(s2)
#       india        #----


s3 = s1.center(20, "x")
print(s3)
#xxxxxxxindiaxxxxxxxx



s1 = "I love my India. Delhi is capital of India."
num = s1.count("India")
print(num)     #2


s1 = "I love my India. Delhi is capital of India."
# Search from position 15 and onwards:
num = s1.count("India", 15)
print(num)     #1



s1 = "I love my India. Delhi is capital of India."
status = s1.endswith(".")
print(status)     #True




s1 = "I\tN\tD\tI\tA"
s2 =  s1.expandtabs(6)
print(s2)
#I     N     D     I     A





s1 = "I love my India. Delhi is capital of India."
num = s1.find("love")
print(num)       #2

num = s1.find("LOVE")
print(num)       #-1




#code2

s1 = "Price of the pen is {price:.2f} rupees!"
print(s1.format(price = 95))
#Price of a pen is 95.00 rupees!







#The placeholders can be identified using named indexes {price},
# numbered indexes {0}, or even empty placeholders {}.


s1 = "My name is {fname}, I'am {age}".format(
                     fname = "Alisha", age = 5)


s2 = "My name is {0}, I'am {1}".format("Alisha",5)


s3 = "My name is {}, I'am {}".format("Alisha",5)








#Check if all the characters in the text is alphanumeric:
s1 = "Jeet123"
status1 = s1.isalnum()
print(status1)        #True


s1 = "Jeet 123"
status1 = s1.isalnum()
print(status1)        #False




s1 = "Jeet123"
status = s1.isalpha()
print(status)        #False


s1 = "Jeet"
status = s1.isalpha()
print(status)        #True




s1 = "1234"
status = s1.isdigit()
print(status)        #True


s1 = "12A34"
status = s1.isdigit()
print(status)        #False



#code 3
s1 = "python is simple."
s2 = s1.capitalize()
print (s2)
#Python is simple.


s1 = "3 is greater than 2."
s2 = s1.capitalize()
print (s1)
#3 is greater than 2.

s1 = "india"
s2 = s1.center(20)
print(s2)
#       india        #----


s3 = s1.center(20, "x")
print(s3)
#xxxxxxxindiaxxxxxxxx



s1 = "I love my India. Delhi is capital of India."
num = s1.count("India")
print(num)     #2


s1 = "I love my India. Delhi is capital of India."
# Search from position 15 and onwards:
num = s1.count("India", 15)
print(num)     #1



s1 = "I love my India. Delhi is capital of India."
status = s1.endswith(".")
print(status)     #True




s1 = "I\tN\tD\tI\tA"
s2 =  s1.expandtabs(6)
print(s2)
#I     N     D     I     A





s1 = "I love my India. Delhi is capital of India."
num = s1.find("love")
print(num)       #2

num = s1.find("LOVE")
print(num)       #-1




#code2

s1 = "Price of the pen is {price:.2f} rupees!"
print(s1.format(price = 95))
#Price of a pen is 95.00 rupees!







#The placeholders can be identified using named indexes {price},
# numbered indexes {0}, or even empty placeholders {}.


s1 = "My name is {fname}, I'am {age}".format(
                     fname = "Alisha", age = 5)


s2 = "My name is {0}, I'am {1}".format("Alisha",5)


s3 = "My name is {}, I'am {}".format("Alisha",5)








#Check if all the characters in the text is alphanumeric:
s1 = "Jeet123"
status1 = s1.isalnum()
print(status1)        #True


s1 = "Jeet 123"
status1 = s1.isalnum()
print(status1)        #False




s1 = "Jeet123"
status = s1.isalpha()
print(status)        #False


s1 = "Jeet"
status = s1.isalpha()
print(status)        #True




s1 = "1234"
status = s1.isdigit()
print(status)        #True


s1 = "12A34"
status = s1.isdigit()
print(status)        #False



#code 3

s1 = "num1"
status = s1.islower()
print(status)        #True



s1 = "   "
status = s1.isspace()
print(status)



s1 = "I love my India"
s2 = s1.replace("India", "INDIA")
print( s2 )






s1 = "I love my India"
arr = s1.split(" ")
print(arr)




arr = ['I', 'love', 'my', 'India']
x = ":".join(arr)
print(x)

#-------------

arr = ['I', 'love', 'my', 'India']
y = ":"
x = y.join(arr)
print(x)






s1 = "123"
s2 = s1.zfill(5)
print(s2)








s1 = "i love my india"
s2 = s1.title()
print(s2)



s1 = "####IN#DIA####"
s2 = s1.strip("#")
print(s2)




s1 = "####---aabbcc.....IN#DIA....dd"

s2 = s1.strip("#-.abcd")

print(s2)
