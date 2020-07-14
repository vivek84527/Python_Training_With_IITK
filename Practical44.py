d = {'A': 'Java', 'B': 'J2EE', 'C': 'Android',
     'D': 'Python', 'E': 'Hadoop', 'Key': 'Value'}

print("d['A'] = ", d['A'])

# print( "d['Z'] = " , d['Z']   )  #Error

print("d.get('Z') = ", d.get('Z', 555))

print("d.get('A') = ", d.get('A', 555))

print("d.get('Z') = ", d.get('Z'))
