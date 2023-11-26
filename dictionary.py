dic = {1: "A", 2 :"B"}

print (dic[1])

print(dic.get(3,"x")) # if the key does't exist --> 3 will return x \ if i put exist key 1 or 2 will return their value A,B
print (dic.pop(1))#works with values
for x in dic:
    print(x)
for x in dic.items():
    print(x)
dic2= {1: {"name":"Ali", "age":23}, 2:{"name":"Muna", "age":22}}

for key in dic2:
    for key1 in dic2[key]:
        print(dic2[key][key1])
#ex: print the name of persons that their age is above 22:         
dic = {1: {"name":"John", "age":27, "six":"Male"},
       2: {"name":"Marie", "age":22, "six":"Female"},
       3: {"name":"Sali", "age":23, "six":"Female"}}

for key in dic:
    if dic[key]["age"] > 22:
        print (dic[key]["name"])