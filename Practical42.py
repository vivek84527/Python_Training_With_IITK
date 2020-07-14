d = {'A': 'Java', 'C': 'Android', 'B': 'J2EE',
     'D': 'Python', 'E': 'Hadoop', 'Key': 'Value'}

keyList = d.keys()

for k in sorted(keyList):
    print(k, d[k])
