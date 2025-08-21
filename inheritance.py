#1st single

class car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")

class Toyotacar(car):
    def __init__(self,name):
        self.name = name

car1 = Toyotacar("Fortuner")
car2 = Toyotacar("prius")

print(car1.start())
        


#2nd multilevel

class car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped..")

class Toyotacar(car):
    def __init__(self,brand):
        self.brand = brand

class fortuner(Toyotacar):
    def __init__(self, type):
        self.type = type
        #super().start()                        #super method use to access of parent method

car1 = fortuner("petrol")
print(car1.type)
        


#3rd class method

class person:
    name = "anonymous"

    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = person()
p1.changename("rahul")
print(p1.name)



#4th property method

class student:
    def __init__(self, phy , chem , math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3)  + "%"
    
stud1 = student(90,88,90)
print(stud1.percentage)


stud1.phy = 60
print(stud1.percentage)