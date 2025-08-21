info ={
    "Name" : "ayan",
    "age"  : 21,
    "subject" : ["python","java","c"]
    
}
info["age"] = 40                # change
info["surname"] = "khabharat"   # insert
print(info)


#1st Dictionary methods 


print(info.keys())
print(info.values())
print(info.items())

info.update({"city" : "meghraj"})
print(info)


#prac Q => enter marks of 3 subj from user and store them in dictionary. start with empty dict & add one by one.use subject name as key & marks as value


subjects = {}

x = int(input("enter phy : "))
subjects.update({"phy": x})

x = int(input("enter che : "))
subjects.update({"che": x})

x = int(input("enter maths : "))
subjects.update({"maths": x})

print(subjects)


#prac Q => store following word meanings in python dictionary


dic = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","list of facts & figures"]
}

print(dic)


