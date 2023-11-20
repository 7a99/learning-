#how to get the sum of the entered number by using function:

n = input ("Enter the num: ")
def sum_digits(x):
    sum_ = 0
    i=n
    while (i!=0):
        sum_+= int(i)%10
        i= int(i)//10
    return sum_

y = sum_digits(n)
print(y)
