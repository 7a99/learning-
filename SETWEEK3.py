x = {4,6,4,1}
y = {1,6,4,1,0,9}
print(x.union(y))
print(x.intersection(y))
x.discard(6)
print(x)

print("############")

z = [[1,2,3],
     [6,7,8]]

v = [[6,1],
     [2,10],
     [0,2]]

def matrix_mult(z,v):
    result = []
    for i in range (len(z)):
        raws =[]
        for j in range (len(z)):
            raws.append((z[i][j])*(v[i][j]))
        result.append(raws)
    print(result)
matrix_mult(z,v)