#1st

#function defination
def calc_sum(a,b):      #parameters
    sum = a + b         
    print(sum)
    return sum
    
calc_sum(5,10)           #function call  ,   5,10 = argument
calc_sum(2,10)



#2nd

def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum / 3
    
    print(avg)
    return avg

calc_avg(2,6,8)    


#3rd

cities = ["Delhi","gurgaon","noida","mumbai","chennai"]
heroes = ["Thor","ironman","captain america"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)



cities = ["Delhi","gurgaon","noida","mumbai","chennai"]
heroes = ["Thor","ironman","captain america"]

def print_list(list):
    for item in list:
        print(item,end=" ")      #list in same line 

print_list(heroes)        



#4th


def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fact(5)     



#5th

def converter(usd_val):
    inr_val = usd_val * 87
    print(usd_val,"USD = ", inr_val,"INR")

converter(10)    



#6th

def find_number(n):
    
    if n%2 == 0:
        print("ODD")
    else:
        print("EVEN")    

find_number(12)
find_number(15)