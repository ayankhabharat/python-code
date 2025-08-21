#1st

#recursive function
def show(n):
    if (n == 0):    #base case means stop
        return
    print(n)
    show(n-1)

show(8)    



#2nd

def fact(n):
    if (n == 1 or n == 0):
        return 1
    return fact(n-1) * n
    
print(fact(5))



#pract Q => recursive function to calculate sum of first n nutural number

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

print(calc_sum(5))



#pract Q => recursive function to print all elements in list

def print_list(list,idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list ,idx+1)

fruits = ["apple","mango","banana","watermalon"]
heroes = ["ironman","thor","captain"]
print_list(heroes)
print_list(fruits)