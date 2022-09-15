#!/usr/bin/env python
# coding: utf-8

# In[1]:


d= {}


# In[2]:


type(d)


# In[3]:


d = {'foo':42}


# In[4]:


d['foo']

List - items in list are Ordered
Dictionary : iten in dictionary are unordered
# In[5]:


spam = {'bar':100}
spam['foo']


# In[6]:


spam ={'cat':100}
'cat' in spam


# In[7]:


'cat' in spam.keys()
There is no differnce, both check if 'cat' is key of the dictionary and if its a key, returns True.


# In[8]:


spam ={'cat':100}
'cat' in spam


# In[9]:


spam ={'cat':100}
'cat' in spam.values()

#'cat' in spam checks whether there is a 'cat' key in the dictionary
#'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.


# In[10]:


spam ={'cat':100}
spam.setdefault('color','black')
spam


# In[15]:


import pprint
dct_arr = [ {'Name': 'Shiva', 'Age': '23', 'Country': 'India'},
  {'Name': 'Anna', 'Age': '44', 'Country': 'China'},
  {'Name': 'Joe', 'Age': '29', 'Country': 'UK'},
  {'Name': 'Chumlee', 'Age': '35', 'Country': 'USA'}]


# In[13]:


pprint.pprint(dct)


# In[16]:


print(dct_arr)


# In[ ]:




