"""
silcing in used to retrieve the elements from one particular range
to another particular range
the syntax:s^3(start:stop:skip)
"""

mylist = [1,2,13,15,16,17,18,19]
print(mylist)
print(mylist[0:6:2])

mylist1=[2,5,6,7,8,9,10]
print(mylist1[0:7:3])

mylist2=[45,56,78,23,56,35,90]
print(mylist2[0:8:4])


mylist4=["hii",12,34,56,899,8987]
print(mylist4[2:6:])


# LIST METHODS

mylist=[1,2,3,45,67,89,567.8,89]
print(mylist)
print(mylist[5])
print(mylist[-4])


# 1. append method
#syntax list variablename.method(
#append method is used to add the elements at the end of the list

fruits=[12, "goa", "sapota"]
print(fruits)

#extend
fruits.append(["hello","edinburgh","UK"])
print(fruits)

#count used to tell about the repested items in a list(one argument at a time)
flowers=["rose", "marigold","rose"]
print(flowers.count("rose"))

#mutabbility(changing the elements)
mylist3=[12,33,44,55,66]
print(mylist3)
mylist3[2]="hello"
print(mylist3)

#pop-- removes te element using a index
mylist5=[12,34,67,89,90]
print(mylist5.pop(2))

#3/7/2025
#remove-- removes the element directly
#that are present in a list
mylist5.remove(34)
print(mylist5)

#count --it is counts the number of occurance of a item in a list
mylist2=[22,44,55,66,77.88j,88,22]
print(mylist2.count(88))

#note; it will take almost only one argument


#insert-- it just inserts the elements into the list
mylist7=[22,33,44,77,88]
print(mylist7)
mylist7.insert(1,"bye")
print(mylist7)


#note :in insert method no element is removed"
#they just replaces the position"
#index method--this method tells the 
#index of first occurance of a element
mylist8=[22,33,44,55,66,67,89,]
print(mylist8.index(44))#1
print(mylist8.index(55))#2

#reverse --it just reveres the elements
mylist8.reverse()
print(mylist8)

#copy--itjust copy the elemnts in a list from 
#one list to other
mylist9=[22,33,44,55,66,77]
print(mylist9)
mylist10=mylist9.copy()
print(mylist10)

#clear--it clears the elements in a list
print(mylist10.clear())
print(mylist10)

#sort-- it just arranges the elements in a sorting way
mylist11=[22,11,77,9,89,0]
mylist11.sort()
print(mylist11)
mylist12=["m","a","c","f","j"] 
mylist12.sort()
print(mylist12)

#mylist13=[12,123,"hello"]
#mylist13.sort()
#print(mylist13)

#in built functions
mylist12=[23,34,56,89]
print(len(mylist12))
print(max(mylist12))
print(min(mylist12))
print(sum(mylist12))


# TUPLES

"""
tuples is a collection of items/values/elements
they are enclosed within the parenthesis or open brackets() seperated by(,)
As tuples are immutable it mean we can't change
so when the data is fixed we can go with tuples..
"""
#eg1:
mytuple = (13,12,11)
print(type(mytuple))#<class tuple
mytuple2=()
print(type(mytuple2))#<class tuple
mytuple3=(10)
print(type(mytuple3))#<class int>


"""
note: when you wanna create a tuple with single valueit should be seperated
by so that the compiler treats as tuple r else it just treats as integer
"""

#creation of tuples
#syntax:tuple variable =(val2,val2,val3..valn)
mytuple5=(12,23,45.5,56+87j,[12,34,],"hi",(123,"ece"))
print(mytuple5)
#creating the tuple with a list
t=mytuple6=(45,)
print(type(mytuple6))
#creating the tuple with a list 
t=[23,45,56,"jj"]
print(t)
k=tuple(t)
print(k)
#creating the tuples with "tuple" predefined word
t=tuple()#it consider as empty tuple
print(t)

"""
#7/4/2025 
tuple used 2 types 1.acessing
                    2.slicing
"""

#Acessing the elements in a tuples
#using the index we can excess the elements in a tuple
#index syntax(start:stop)
mytuple8=(11,22,33,44,55,(78,89),"hello")
print(type(mytuple8))
print(mytuple8[0:5])
print(mytuple8[0:3])

mytuple9=(11,22,[33,44,55,88],(99,67))
print(mytuple9[2])


"""
silcing in used to retrieve the elements from one particular range
to another particular range
the syntax:s^3(start:stop:skip)
"""

mytuple10=(11,12,33,44,55,77,88,99,"ece","hi","hello")
print(mytuple10[3:9:3])

mytuple11=(22,33,444,66,77,88,99,10,24,45,67,45,78)
print(mytuple11[4:10:5])

#indexes are of 2 types 
# 1.positive indexing or forward indexing which always start with 0 from left hand side direction
# 2.negative indexing or backward indexing which always start with 0 to right hand direction.

mytuple12=("hello",123,456,45,34.45,56+76j,"ists","agri","ece",345.9,"dept",12,23,
           34,56,67,90)
print(mytuple12[-1])
print(mytuple12[2:-2:2])

#9/7/2025

mytuple = (10,[12,13],[23,56])
print(mytuple [1][1])
print(mytuple [2][1])

mytuple2 = (12,13,14,(16,17,18),(19,20,22))
print(mytuple2 [4][2])


# concatenation

"""
this operator is used to concatenate the values 
"""


# repition operator * (astric)
"""
this operator is used to repeat a given values 
"""

m = (2,3,4)
n = m*3
print(n)

#len()
"""
this function is determine the length of the value 
"""
s=(3,4,5)
print(len(s))

# count()-->pyrathasis count of
"""
this function is usedto count the number of repeted values in a given seguence
"""
g=(1,2,3,4,3,3)
print(g.count(4))

#index()-->it is read index off by using pyrathasis


