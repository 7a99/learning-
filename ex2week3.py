x =5

def add_num (x):
    x += 2
    return x

print (x) # call by value
print (add_num(x)) #call by reference

matrix = [[2,5,1],
          [6,8,0],
          [4,9,7]]
count =0
# print (matrix[1][1])# 1 row 1 column
for i in range (len(matrix)):
    for j in range (len(matrix)):
        print (matrix[i][j]*2, end = " ")
    print ()
    
