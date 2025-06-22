"""
 a if within a if it is called nested if
 Note:in order to execute inner else outer if condition must be true
 syntax:
 if condition:
    outer if statements
    if codition:
    inner if statements
    else:
    inner else statements
else:
    outer else statements
"""  

     






a=12
b=20
c=30
if a==12 and c==30:
    print("the outer if executed..")
    if a==12:
        print("the inner if executed..")
    else:
        print("the inner else executed..")
else:
    print("the outer else executed..")