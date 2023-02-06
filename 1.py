#!/usr/bin/env python
# coding: utf-8

# In[2]:


def count_socks(socks): 
    socks_count = {} 
    for sock in socks: 
        if sock in socks_count:
            socks_count[sock] += 1
        else:
            socks_count[sock] = 1
    return sum(count//2 for count in socks_count.values())

a. Input: [10 20 20 10 10 30 50 10 20]
   Output yang diharapkan: 3
# In[4]:


socks = [10,20,20,10,10,30,50,10,20]
print(count_socks(socks))

b. input: [6 5 2 3 5 2 2 1 1 5 1 3 3 3 5]
   Output yang diharapkan: 6
# In[5]:


socks = [6,5,2,3,5,2,2,1,1,5,1,3,3,3,5]
print(count_socks(socks))

c. Input: [1 1 3 1 2 1 3 3 3 3]
   Output yang diharapkan: 4
# In[6]:


socks = [1,1,3,1,2,1,3,3,3,3]
print(count_socks(socks))

Thankyou ^-^