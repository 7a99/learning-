def func1(t):
    t = t * 2
    
t =(1,2,3)
print (t)
func1(t)
print(t.count(1))
print(t.index(1))

ls = set ([1,2,4,2])
print(ls) # set doesn't except repeat element
ls.add(3)
ls.update()
print(ls)