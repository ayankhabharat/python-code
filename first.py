#1st string and len

str1 = "ayan"
len1 = len(str1)
print(len1)



#2nd index

str = "my name is ayan"
char = str[0]
print(char)


#3rd slicing

str = "my name is ayan"
print(str[1:7])                      #index start is 01234..  [start_index :end_index]



#4th .endswith() function

str = "my name is ayan"
print(str.endswith("ayan"))



#5th .capitalize() function

str = "my name is ayan"
print(str.capitalize())



#6th  .replace() function

str = "my name is ayan"
print(str.replace("a","o"))




#practice question =  WAP  to input user's first name & print its length

Name = input("enter your name :")
print("length of name is ",len(Name))


#practice question =  WAP  to find the occurrence of "$" in string

str = "hello i am $ symbol to i give you $100 cash and $400 in your acc "
print(str.count("$"))