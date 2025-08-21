student = ["karan",95.4 ,17,"delhi"]
print(student) 

#1st list method  (.append), (.sort)

list = [3,2,5,4,8,7]
list.append(9)
print(list)

print(list.sort())                          #ascending order
print(list)

print(list.sort(reverse=True))              #descending order
print(list)

print(list.reverse())
print(list)


#2nd list method (.reverse), (.insert) , (.remove) , (.pop)

list = ["a","c","f","e","d","r"]
list.reverse()
print(list)


list = [2,4,1,5]
list.insert(1,7)                #(index ,element)
print(list)


list.remove(4)
print(list)

list.pop(3)         #(index)
print(list)





#Tuples method      (.index), (.count)

tup = (1,2,3,4,2,7,2)
print(tup.index(2))         #(2 = element  and output is index)


print(tup.count(2))



#practice Q => WAP to ask user to enter names of their 3 favorite movies & store them in list

movies = []

movies.append(input("enter first movie :"))
movies.append(input("enter second movie :"))
movies.append(input("enter third movie :"))


print(movies)


#practice Q => WAP to check if list contains palindrome of element

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")


#practice Q => WAP to store the above values in list & sort them from "A" to "D"

grade = ["a","c","d","b","e","b","a"]
grade.sort()
print(grade)