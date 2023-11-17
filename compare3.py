a = int(input("Enter the 1st num"))
b = int(input("Enter the 2nd num"))
c = int(input("Enter the 3rd num"))

if (a>=b and a>=c):
    print(str(a)+" is the gratest num")
elif(b>=a and b>=c):
    print(str(b)+" is the gratest num")
else:
    print(str(c)+" is the gratest num")