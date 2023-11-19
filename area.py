
#tringle area
base1= int(input("Enter the base of tringle: "))
h1=int(input("Enter the hight: "))

def tringle_area(base1, h1):
   area1 = 1/2 * base1* h1
   return(area1)

#sequare area

side1=int(input("Enter the side of sequare: "))
def sequare_area(side1):
    area2 = side1* 2
    return(area2)
       
#circle area (π r²)
PI = 3.14
r = int(input("Enter the r value: "))
def circle_area(PI,r):
    area3 =( PI * (r**2))
    return(area3)

#cylinder area (2π r h + 2π r²)
PI =3.14
r1 = int(input("Enter the r value: "))
h2 = int(input("Enter the hight: "))

def cylinder_area(PI,r1,h2):
    area4= ((2 * PI * r1) + 2*PI (r1**2))
    return(area4)
    