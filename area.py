
# functions
def tringle_area(base1, h1):
   area1 = 1/2 * base1* h1
   return(area1)

#sequare area
def sequare_area(side1):
    area2 = side1* 2
    return(area2)

#circle area (π r²)
def circle_area(PI,r):
    area3 =( PI * (r**2))
    return(area3)

#cylinder area (2π r h + 2π r²)
def cylinder_area(PI,r1,h2):
    area4= ((2 * PI * r1) + 2*PI (r1**2))
    return(area4)



while 1:
     
    # read user choice
    choice = input("Enter choice (1 ,2 ,3 ,4 ,Q): ")

    # if choice 1 --> triangle
    if choice=="1":
        # base?
        base1= int(input("Enter the base of tringle: "))
        # height?
        h1=int(input("Enter the hight: "))
        # call triangle fucntion and give it the parameters
        print("the area of the triangle = " ,tringle_area(base1, h1))

    elif choice =="2":
        side1=int(input("Enter the side of sequare: "))
        print(sequare_area(side1))

    elif choice =="3":    
        PI = 3.14
        r = int(input("Enter the r value: "))
        print(circle_area(PI,r))
        
    elif choice =="4":
        PI =3.14
        r1 = int(input("Enter the r value: "))
        h2 = int(input("Enter the hight: "))
        print(cylinder_area(PI,r1,h2))

    elif choice.upper() == "Q":
        break
    
    else:
        print("wrong choice!!")    
    
