# 1st

class car:
    color = "red"
    brand = "ferrari"

car1 = car()
print(car1.color)


#2nd Default constructor (__init__)

class student:
    def __init__(self,name,marks):            #constructor   name,marks = parameter
        self.name = name                      #self.name = object creat
        self.marks = marks
        print("adding new student")

s1 = student("ayan",97)
print(s1.name,s1.marks)

s1 = student("masud",96)
print(s1.name,s1.marks)



#prac Q => Create student class takes name & marks of 3 subjects as argument in constructor.then create method to print average

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
   
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name,"your avg score is :",sum/3)
    

s1 = student("Tony stark", [88,89,95])
s1.get_avg()

s1.name = "Ayan"
s1.marks = 90,90,100
s1.get_avg()



#4th abstraction

class car():
    def __init__(self):                         #process of car is strate
        self.acc = False
        self.brk = False                            
        self.clutch = False

    def start(self):                             #process to car start
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = car()                                     #when car is start only show to "car started"
car1.start()



##prac Q => Create account class with 2 attributes-balance & acccount no. create method for dr,cr&printing balance


class account:

    def __init__(self, acc , bal):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was Debited")
        print("Total Balance = ",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was Credited")
        print("Total Balance = ",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = account(99789 , 20000)
acc1.debit(5000)
acc1.credit(399)
acc1.debit(5089)



#6th  private method

class person:

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()

p1 = person()
print(p1.welcome())                                  #if you print(p1.__hello)= error  


