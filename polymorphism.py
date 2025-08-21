#1st Dunder function  (__add__)  (__sub__)

class complex:
    def __init__(self, real , img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i+", self.img, "j")

    def __sub__(self,num2):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return complex(newreal , newimg)
    
    def __add__(self,num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newreal , newimg)


num1 = complex(1,3)
num1.shownumber()
        
num2 = complex(8,5)
num2.shownumber()

# num3 = num1.add(num2)
# num3.shownumber()

num3 = num1 + num2      #add
num3.shownumber()

num3 = num1 - num2      #sub
num3.shownumber()




#2nd    define area and perimeter
class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = circle(12)
print(c1.area())
print(c1.perimeter())
        


#3rd        create class employee and showdetail . create engineer class add employee class 

class employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept 
        self.salary = salary
    
    def showdetails(self):
        print("role = ",self.role)
        print("dept = ",self.dept)
        print("salary = ",self.salary)

class engineer(employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("engineer","IT","60,000")
        
# E1 = employee("Accountant","Finance","50,000")
# E1.showdetails()

eng1 = engineer("ayan",21)
eng1.showdetails()




#4th        create order class to store item and price .use Dunder function  __gt__()

class order:
    def __init__(self, item , price):
        self.item = item
        self.price = price
    
    def __gt__(self ,ord2):
        return self.price > ord2.price
    
ord1 = order("chip",20)
ord2 = order("Tea",15)

print(ord1>ord2)