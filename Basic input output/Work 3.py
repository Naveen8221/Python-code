#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Enter a number between (1-12) and print respective month.
num=int(input("Enter the number"))
if num==1:
    print('january')
elif num==2:
    print("February")
elif num==3:
    print("March")
elif num==4:
    print("April")
elif num==5:
    print("May")
elif num==6:
    print("June")
elif num==7:
    print("July")
elif num==8:
    print("August")
elif num==9:
    print("September")
elif num==10:
    print("October")
elif num==11:
    print("November")
elif num==12:
    print("December")  
else:
    print("not valid")


# In[2]:


# Enter a number between (1-4) and perform operations Add.,Sub.,Mul.,Div.
enter=int(input())
num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
if enter == 1:
    print("Addition")
    num3=num1+num2
    print(num3)
elif enter  == 2:
    print("Subtraction")
    num3=num1-num2
    print(num3)
elif enter == 3:
    print("Multiplication")
    num3=num1*num2
    print(num3)
elif enter == 4:
    print("Division")
    num3=num1/num2
    print(num3)
else:
    print("not valid")

