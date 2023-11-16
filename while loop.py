start = 1
n =int (input("Enter the num:"))
sum_ =0
while(start<=n):
    sum_+=start
    start+=1
print (sum_)

#how to get the sum of the entered number as a string
i = 0
n =(input("Enter the num:"))
sum_ =0
while(i<len(n)):
    sum_+=int(n[i])
    i+=1
print (sum_)

#how to get the sum of the entered number as an integer

n = input ("Enter the num: ")
sum_ = 0
while (n!=0):
    sum_+= int(n)%10
    n= int(n)//10
print (sum_)
