list1 = [20, 10, 30, 100, 90, 70]

list2 = sorted(list1)  # External Sorting

print("list2 = ", list2)
print("list1 = ", list1)

list1.sort()  # In-place or internal sorting
print("list1 = ", list1)

tx = (20, 10, 30, 100, 90, 70)
ty = sorted(tx)  # In-place Sorting is not allowed in tuple
print("tx = ", tx)
print("ty = ", ty)

# tx.sort()  #Invalid because tuple is immutable
