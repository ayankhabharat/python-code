# 1st

i = 1
while i<=10:
    print("ayan",i)
    i+=1
print(i)    


#2nd  multiplication table of number n

i = 1
n = int(input("enter of number: "))
while i<=10:
    print(n*i)  
    i += 1



#3rd print the element of list using loop

nums = [1,2,4,6,8,5,10,22,55,100]
idx = 0
while idx < len(nums):
    print(nums[idx], idx)           #idx=len ,nums[0],nums[1]
    idx += 1




#4th search for number x

nums = [1,2,4,6,8,1,5,10,22,55,100]
x = 22
idx = 0
while idx < len(nums):
    if(nums[idx] == x):
        print("got it ",idx)   #find the number of x
    idx += 1



#5th

i = 0
while i <= 10:
    if (i == 4):
        i += 1
        continue     #skip 4 number and another continue
    print(i)
    i += 1