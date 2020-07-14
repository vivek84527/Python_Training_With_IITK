alpha = input("Enter alphabet to search : ")  # D

for ch in "ABCDE":
    if ch == alpha:  # alpha = 'D'
        print(alpha, "found is the given word")
        break
else:
    print(alpha, "not found is the given word")
