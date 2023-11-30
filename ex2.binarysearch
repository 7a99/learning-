def binary_search(x):
    law, hight=1, x
    if (x ==1 or x ==0):
        return x
    while law <= hight:
        mid =( law + hight)//2
        if mid*mid== x:
            return mid
        elif x > mid*mid:
            law =  mid +1
        else:
            hight = mid -1
    return -1

result=binary_search(25)
print(result)
