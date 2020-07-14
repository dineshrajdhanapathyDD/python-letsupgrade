#!/usr/bin/env python
# coding: utf-8

# # errors using Exception Handling

# In[ ]:


#For this challenge you need to develop a Python program to open a file in read only mode and try writing
#something in it and handle the subsequent errors using Exception Handling.


# In[1]:


file = open("FCS.txt",'w')
file.write("I LOVE FCS")
file.close()


# In[2]:


try:
    file = open("FCS.txt",'r')
    file.write("ABC")
except Exception as e:
    print("The file gave us error - ", e)
    file = open("FCS.txt",'r')
    print(file.read())
finally:
    file.close()


# In[3]:


get_ipython().system('pip install pylint')


# # question2

# In[4]:


#Write a python Function for finding a given number prime or not and do Unit Testing on it using PyLint &
#Unit test Library.


# In[40]:


def test_prime(n):
    if (n==1):
        return Flase 
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
    return True            
print(test_prime(2))


# In[12]:


get_ipython().run_cell_magic('writefile', 'testprimenumber.py', "def test_prime(n):\n    '''\n    1. A prime number (or a prime) is a natural number\n    '''\n    if (n == 1):\n        return False \n    elif (n == 2):\n        return True\n    else:\n        for x in range(2,n):\n            if(n % x == 0):\n                return False\n    return True            \nprint(test_prime(2))")


# In[13]:


get_ipython().system('pylint testprimenumber.py')


# In[5]:


get_ipython().run_cell_magic('writefile', 'unittest_Prime.py', "import unittest\nimport testprimenumber\n\nclass Testprime(unittest.TestCase):\n    \n    def test_prime(self):\n        \n        result = testprimenumber.test_prime(2)\n        self.assertTrue(True)\n        \n    \n    \nif __name__ == '__main__':\n    unittest.main()")


# In[6]:


get_ipython().system(' python unittest_Prime.py')


# In[ ]:




