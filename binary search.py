def binary_search (target,x):
    law = 0
    hight=len(x)-1

    while law <= hight:
        mid =( law + hight)//2
        if x[mid] == target:
            return (mid)
        elif target < x[mid]:
            hight = mid -1
        else:
            law =  mid +1
    return -1

x = [15,4,7,5,8,9,12,2]
x.sort()
print(x)
target = int (input("Enter the target: "))
result =binary_search(target, x)
print("the indix of your target is: ",result)