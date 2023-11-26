# how to count number of zeros in a matrix
matrix = [[0,5,1],
          [6,8,0],
          [4,0,7]]
count =0
for i in range (len(matrix)):
    for j in range (len(matrix)):
        if  matrix[i][j] == 0:
            count += 1
print(count)

print("#############################################")

# how to sum two 2d matrix and append the result in new matrix
m1 =[[0,5,1],
    [6,8,0],
    [4,0,7]]

m2 =[[5,5,6],
    [2,3,4],
    [7,8,2]]

def sum_matrix(m1,m2):
    result = []
    for i in range (len(m1)):
        raws =[]
        for j in range (len(m1)):
            raws.append(m1[i][j]+m2[i][j])
        result.append(raws)
    print(result)
sum_matrix(m1,m2)

print("#############################################")
# how to print:
# 1 1 1 1 
# 0 1 1 1 
# 0 0 1 1 
# 0 0 0 1

size = int (input("Enter the size: "))

for i in range (size):
    for j in range (size):
        if j>= i:
            print (1, end = " ")
        else:
            print (0, end = " ")
    print()