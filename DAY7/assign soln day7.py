#!/usr/bin/env python
# coding: utf-8

# # day 7 QUESTION1

# In[1]:


#Write a decorator function for your taking input for you any kind of function you want to build
#For example - you make a fibonacci series function, in which your input range is
#been defined by the decorator programs input.


# In[3]:


def getInput(some_Func):
    def fib(n):    # write Fibonacci series up to n
    #"""Print a Fibonacci series up to n."""
        a= int(input("enter a number")) #0
        b= int(input("enter b number")) #1
    #while a < n:
        #print(a, end=' ')
        #a, b = b, a+b
        #fib(n)
        some_Func(a,b,n)
    fib(int(input("enter n"))) 


# In[6]:


@getInput
def loop(a,b,n):
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
#fib(n)


# In[ ]:





# In[ ]:




