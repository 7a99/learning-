class Math:
    @staticmethod
    def add_numbers(x,y):
        return x+y
    @staticmethod
    def pi():
        return 3.14
class Shape:
    def __init__(self, name, color, radius):
        self.name=name
        self.color=color
        self.radius=radius
        
    def area_shape(self):
        return 2*Math.pi()*self.radius
    
sh = Shape ("c1","red", 4)
print(sh.area_shape())
print(Math.add_numbers(3,5))

class Numbers:
    def __init__(self):
        self.numbers =[]
        
    def add_num (self, num):
        self.numbers.append(num)
        
    def sum_numbers(self):
        sum_ = 0
        for i in self.numbers:
            sum_ += i
        return sum_
n1 = Numbers()
n1.add_num(2)
n1.add_num(3)
print(n1.sum_numbers())