d = {'A': 'Java', 'B': 'J2EE', 'C': 'Android',
     'D': 'Python', 'E': 'Hadoop', 'Key': 'Value'}

print("dictionary = ", d)

d['F'] = 'JAPAN'
print("dictionary = ", d)

d['B'] = 'INDIA'
print(d)

del d['E']
print(d)

# Dictionary do not support positional access .
# print(D[0]) iTS SHOW Error

status = 'C' in d
print(status)