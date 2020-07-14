#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Make only one class with functions, as in where required Import Math
import math
class cone:
    def __init__(self,radius,height):
        self.radius = 0
        self.height = 0
    def volume(self):
        self.radius = int(input("radius of cone"))
        self.height = int(input("height of cone"))
        volume1 = (math.pi*self.radius*self.radius*self.height/3)
        print(volume1)
    def surfacearea(self,base,side):
        self.base =0
        self.side=0
    def surfacearea(self):
        self.base = int(input("base of cone"))
        self.side = int(input("side of cone"))
        surfacearea = (math.pi*self.radius*math.sqrt(self.radius*self.radius *self.height*self.height))
        print(surfacearea)


# In[23]:


s=cone(2,2)


# In[24]:


s.volume


# In[26]:


s.volume()


# In[27]:


s.surfacearea()


# In[27]:


#As an added requirement, withdrawals may not exceed the available balance.
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class bank_Account:
    def __init__(self):
        self.owner = "DD"
        self.balance = 10000
        print("welcome")
    
    def deposit(self):
        amount=float(input("enter the amount deposit"))
        self.balance += amount
        print("amount deposit=",amount)
    def withdraw(self):
        amount=float(input("enter the amount withdraw"))
        if self.balance >= amount:
            self.balance -= amount
            print("you withdraw amount",amount)
        else:
            print("insufficient balance")
            
    def display(self):
        print("net available balance=",self.balance ,"\n owner=" ,self.owner)
        


# In[28]:


s=bank_Account()


# In[29]:


s.display()


# In[30]:


s.deposit()


# In[31]:


s.display()


# In[ ]:




