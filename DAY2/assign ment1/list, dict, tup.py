#!/usr/bin/env python
# coding: utf-8

# # list

# In[1]:


lst= ['physics', 'Biology', 'chemistry', 'maths']


# In[2]:


lst.append(1)


# In[3]:


lst


# In[4]:


lst.count(1)


# In[5]:


lst.pop()


# In[6]:


lst


# In[7]:


lst.remove('chemistry')


# In[8]:


lst


# In[11]:


lst.sort()


# In[12]:


lst


# In[13]:


lst.reverse()


# In[14]:


lst


# In[17]:


lst.insert(1,'chemistry')


# In[18]:


lst


# In[19]:


lst.index('chemistry')


# In[27]:


lst


# In[33]:


lst.clear()


# In[34]:


lst


# # dictionary

# In[47]:


dict = {'name': 'DD','age':'28'}


# In[46]:


len(dict)


# In[49]:


type(dict)


# In[50]:


dict.clear()


# In[51]:


dict


# In[63]:


dict = {'name': 'DD','age':'28'}
dict.fromkeys(dict,10)


# In[64]:


dict.get('age')


# In[66]:


dict.items()


# In[68]:


dict.keys()


# In[73]:


dict.setdefault('name')


# In[77]:


dict2= {'sex':'male'}


# In[78]:


dict.update(dict2)


# In[79]:


dict


# In[81]:


dict.values()


# In[87]:


dict.pop('sex')


# In[92]:


dict


# In[94]:


dict2= {'sex':'male'}


# In[95]:


dict2.popitem()


# # tuple

# In[137]:


tup = 'i', 'am', 'python', 'learner', 'of', 'letsupgrade'


# In[138]:


tup


# In[139]:


tup.count('i')


# In[140]:


tup.index('python')


# In[113]:


tup2 = (1,2,3,4,5,6,)


# In[119]:


max(tup2)


# In[121]:


min(tup2)


# In[122]:


min(tup)


# In[144]:


max(tup)


# In[143]:


tuple(tup)


# In[134]:


tup2


# # strings

# In[153]:


str('hello')


# In[154]:


str= '''i am dineshraj,
        i am leaner of python,
        learning in letsupgrade'''


# In[155]:


str


# In[156]:


str.(lower)


# In[157]:


#string array
str = 'hello world'
str[2]


# In[158]:


str[2:5] #slicing


# In[159]:


str[-2:-1] #negative indexing


# In[160]:


len(str) #string length


# In[161]:


str.strip() #string methods


# In[162]:


str.upper() #uppercase


# In[163]:


str.lower() #lowercase


# In[164]:


str.replace('h', 'c')


# In[167]:


str.split(",")


# In[168]:


a= 'hello'
b=' world'
c= a+b


# In[169]:


c


# In[170]:


c = a+" "+b


# In[171]:


c


# In[177]:


name = 'dd'
str =  "my name is " + name 
str


# In[179]:


str


# In[179]:


str

