#1st 

light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

print("end of code")


#2nd

marks = int(input("enter student marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of student ->",grade)



#practice Q =>  WAP check if a number entered by the user is odd or even

number = int(input("enter the number : "))

rem = number % 2
if(rem == 0):        #(number %2 == 0)
    print("EVEN")
else:
    print("ODD")



#practice Q =>  WAP to find greatest of 3 numbers entered by the user

a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest",b)
else:
    print("third number is largest",c)



#practice Q =>  WAP to check if a number is multiple of 7 or not

x = int(input("enter number : "))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")