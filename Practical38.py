# Arbitrary Argument List

def disp1(*arr):
    print("type(arr) = ", type(arr), arr)
    print("len(arr) = ", len(arr))
    for num in arr:
        print(num)


disp1(5, 6, 7, 8)
disp1(2, 3)
disp1()
disp1(9)
