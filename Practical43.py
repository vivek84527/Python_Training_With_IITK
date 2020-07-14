d = {'A': 'Java', 'C': 'Android', 'B': 'J2EE',
     'D': 'Python', 'E': 'Hadoop', 'Key': 'Value'}

print("d.items() = ", d.items())

print("Data type =", type(d.items()))

for key, value in d.items():  # [ ( ,),  (,), (,), (,), (,), (,)   ]
    print(key, " = ", value)
