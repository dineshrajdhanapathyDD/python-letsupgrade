#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# WAP for taking one number a input and then using if elif else concept, assign a grade to the input number from


# In[ ]:


marks=int(input("Enter your Marks:"))
print("Your marks is:", marks)
if marks > 75: 
    print ("Your grade is:|A|")
elif marks > 35 and marks < 75: 
    print("Your grade is:|B|")
else:
    print("Your grade is:|FAIL|")
    


# In[ ]:


#WAP gives you a random score of Team India in a cricket match, and a player has to guess the score given by computer in between 1 to 250.


# In[32]:


import random

player = int(input("enter your guess score"))

comp_Score = random.randint(1,250)
print("predicted score by comp", comp_Score)
while player < 1 or player >250:
    print("reduce your expectation of 20-20 cricket")
    break
if player ==(random.randint(comp_Score-10, comp_Score+10)):
    print("close by , you are true indian fan")
else:
    print("you didnt watch match")


# In[ ]:


#WAP to handle file to python script


# In[51]:


file =open("FCS.txt", 'w')
print(file)


# In[57]:


file = open("FCS.txt",'w')
file.write("I LOVE FCS")
file.close()


# In[59]:


file = open("FCS.txt", "r")
text = file.read()
print(text)
file.close()


# In[ ]:





# In[ ]:




