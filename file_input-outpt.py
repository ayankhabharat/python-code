#1st

f = open("demo.txt","r")           #open file ("name","mode")
data = f.read()                      #.read = read file   .readline = read one line
print(data)
f.close()                              #close file when your work is end



#2nd

f = open("demo.txt","w")
f.write("yes i am")                     #change .txt file direct


#3rd

import os

os.remove("")                             #delete file



#4th

with open("demo.txt","w") as f:            #open and change
    f.write("hi everyone .\nwe are learning python and file i/o \n")
    f.write("using vs code")




#pract Q => WAF replace all occurences of "python" with "java" in file

with open("demo.txt","r") as f:
    data = f.read()

new_data = data.replace("python" , "java")
print(new_data)

with open("demo.txt","w") as f:
    f.write(new_data)


#pract Q => WAF search if the word "learning" exists in the file or not

word = "learning"
with open("demo.txt","r") as f:
    data = f.read()
    if(word in data):
        print("found")
    else:
        print("not found")



#pract Q => WAF to find in which line of the file does the word "learning" occur first

def check_for_line():
    word = "learning"                            #find word
    data = True
    line_no = 1
    with open("demo.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
        return -1
check_for_line()



# pract Q => from file containing numbers separated by comma,print the count of even number

count = 0
with open("demo.txt","r") as f:
    data = f.read()

    num = data.split(",")
    for val in num:
        if(int(val) %2 == 0):
            count += 1
print(count)
