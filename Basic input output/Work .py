#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Frist Character in string
Process="Computer"
print(Process[0])


# In[11]:


#Last Character in string using len function
process="Enter the Data"
print(len(process))


# In[2]:


# Last Character in string
process='Enter the Data'
print(process[13])


# In[12]:


# Fetch the 7th element of the string 
Data="We can not update because it is immatuable"
print(Data[7])


# In[13]:


#Fetch all Characters from 0 to 5 index location excliding the character at loc 5.
Data="We can not update because it is immatuable"
print(Data[0:5])


# In[4]:


# Retrieve all characters between 6-12 index ecluding loc 12.
Data="We can not update because it is immatuable"
print(Data[6:12]


# In[17]:


#retrieve last four characters of the string 
Data="We can not update because it is immatuable"
print(Data[-4:len(Data)])


# In[18]:


#retrieve last six characters of the string
Data="We can not update because it is immatuable"
print(Data[-6:len(Data)])


# In[9]:


if __name__ == '__main__':
    n = int(input().strip())
    if n%2==0:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")
    else:
            ("Weird")               
        
     


# In[3]:


i=[i**2 for i in range(10)]
print(i)


# In[2]:


i=[6,5,2,4,1,8,9,7,3]
il=[i*10 for i in i]
print(il)


# In[26]:


print("I am Naveen from loharu distic bhiwani .My father name is sube singh  he is a small scale businessman and my mother name is silochna she is home maker. I am pursuing btech in mechanical branch. Now, i am doing data analyst course last 1 month.")


# In[3]:


#Addition
x=int(input())
y=int(input())
Addition=x+y
print(Addition)


# In[6]:


#subtraction
x=int(input())
y=int(input())
subtraction=x-y
print(subtraction)


# In[7]:


#multiplication
x=int(input())
y=int(input())
multiplication=x*y
print(multiplication)


# In[1]:


#division
x=int(input())
y=int(input())
division=x/y
print(division)


# In[3]:


#modulus
x=int(input())
y=int(input())
modulus=x%y
print(modulus)


# In[4]:


#Exponent
x=int(input())
y=int(input())
exponent=x**y
print(exponent)


# In[7]:


#Swap two number
x=10
y=20
tem=x
x=y
y=tem
print(x)
print(y)


# In[8]:


#swap teo number without third variable
x=20
y=10
x,y=y,x
print(x)
print(y)


# In[11]:


#simple interet
p=int(input())
r=int(input())
t=int(input())
si=(p*r*t)/100
print(si)


# In[12]:


#Average of five number
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())
average=(num1+num2+num3+num4+num5)/5
print(average)


# In[15]:


#discriminant of a quadratic equation
a=int(input())
b=int(input())
c=int(input())
discriminant=(b**2)-4*a*c
print(discriminant)


# In[16]:


#Area of rectangle
l=int(input())
w=int(input())
rectangle=l*w
print(rectangle)


# In[17]:


#Area of square
a=int(input())
square=a**2
print(square)


# In[18]:


#Area of triangle
b=int(input())
h=int(input())
triangle=(1/2)*b*h
print(triangle)


# In[19]:


#Area of circle
r=int(input())
circle=(3.14)*(r**2)
print(circle)


# In[20]:


#power
num=int(input())
power=num**2
print(power)


# In[21]:


#python version
from platform import python_version

print(python_version())


# In[25]:


#Net salary
basic=int(input())
da=basic*0.05
hra=basic*0.07
pf=basic*0.03
net=da+hra+pf
print(net)

