#CONDITIONAL STATEMENTS#

"""
The python conditional making statements are used in order to execute a block of code 
They are "3" types:
1.Decision  making statements
2.Looping/Iterative statements
3.Jumping/transfer statements
"""
 
"""
1.Decison making:
The python decision making statements are used in order execute a particular conditions
they are "5" types  of blocks:
1.if - block
2.if - else
3.else if(elif)
4.nested if
5.shorthand if else
"""

"""
if
the python if block is executed when the condition is true
syntax:
if condition:
    statements
"""

#program#
a = 10
if a==10:
   print("the if statements is executed... ")

   """
   IF ELSE 
   if the condition in "if" statements is failed
   then else block is executed

   syntax:
   if condition:
     statements
     else:
       statements
   """

#program for voter age
age = int(input("enter a age"))
if age>=18:
   print("eligibility for vote",age)
else:
   print("sorry!!no eligible because your age is ,age")