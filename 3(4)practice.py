#while by use


#write a program print 100 numbers

i=0
while i<=99:
    i+=1
    if i==50:
        continue
    print(i)

#nested is use

#write a program vegetarians and non vegetarions

ret=True
order=int(input("enter no of customers"))
if order<=5:
    print("the custmer is order vegetarian")
    if order>=10:
        print("the customer is nonvegetarian")
    else:
        print("the customer is vegetarian but order juices")
else:
    print("the customer is not order")
    


