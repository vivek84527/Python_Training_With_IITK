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
