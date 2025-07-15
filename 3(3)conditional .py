"if"
"""
if condition:
    statement
"""


# write a python program to find whether a number is positive or not

num = int(input("enter a number.."))
if num>0:
    print("the number is positive",num)
else:
    print("the number is negative",num)
#   space is called intentation

# write a program to find biggest of 2 numbers(logic)#
 
a =  int(input("enter a number:"))
b = int(input("enter a number:"))
if a>b:
    print("a is greater :",a)
else:
    print("b is greater :",b)


#accept the percentage from the user and display the grade according to the following criteria tcs(nija,dilite,3 rounds)
"""
BelowD - 25
25 to 45 -- c
45 to 50 -- B
50 to 60 -- B+
60 to 80 --A
above 80+ -- A+
"""
pr = int(input("enter a percentage.."))
if pr<25:
    print("the grade is D..")
elif pr>25 and pr<=45:
    print("the grade is c..")
elif pr>45 and pr<=50:
    print("the grade is B..")
elif pr>50 and pr<=60:
    print("the grade is B++..")
elif pr>60 and pr<=80:
    print("the grade is A..")
elif pr>80:
    print("the grade is A+..")
else:
    print("your failed")

# write a program to display the week names by taking input from the user?

d = int(input("enter a d.."))
if d==1:
    print("sunday")
elif d==2:
    print("monday")
elif d==3:
    print("tuesday")
elif d==4:
    print("wednesday")
elif d==5:
    print("thursday")
elif d==6:
    print("friday")
elif d==7:
    print("saturday")

# write a program to display the monuments
# according to city given by user

mu = input("enter a mu")
if mu=="bangalore":
    print("rose garden")
elif mu=="hyderabad":
    print("charminar")
elif mu=="agra":
    print("taj mahal")
elif mu=="chennai":
    print("marine beach")
elif mu=="delhi":
    print("red fort")
elif mu=="mumbai":
    print("gate way of india")
else:
    print("wrong mu selected")


