#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64

# Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]

list1 = [12, -7, 5, 64, -14]

list2 = [12, 14, -95, 3]

l = len(list1)
for i in range(0,l):
    if list1[i] > 0:
        print(list1[i], ",", end = "")
print()
        
l = len(list2)
for i in range(0,l):
    if list2[i] > 0:
        print(list2[i], " ", end = "")

