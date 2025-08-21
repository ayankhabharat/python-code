#1st

nums = (1,2,3,45,55)    #() = tuple
for val in nums:
    print(val)



#2nd

nums = [1,4,9,16,25,36,49,64,81,100]      #[] = list
for el in nums:
    print(el)



#3rd

nums = (1,4,9,16,25,36,49,64,81,100,49)
x = 49
idx = 0

for el in nums:
    if(el == x):
        print("number is found", idx)
    idx += 1



#4th range()

for i in range(10):
    print(i)

for i in range(2, 20, 2):       # 2 = start , 20 = stop , 2 = add
    print(i)


#5th

n = int(input("enter number :"))

for i in range(1,11):
    print(n * i)


#prac Q => WAP to find sum of first n number

n = 5
sum = 0
for i in range(1, n + 1):
    sum += i
    
print("total sum of :", sum)

    


n = 6
sum = 0
i = 1
while i<= n:
    sum += i
    i += 1
    
print("total sum of :", sum)




#prac Q => WAP factorial of first n number

n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
    

print("total factorial of :", fact)


n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
    
print("factorial :", fact)