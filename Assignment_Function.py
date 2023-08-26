#!/usr/bin/env python
# coding: utf-8

# # Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.
# 
# # Your Input and output should look something like this
# 
# # Input : Please enter a string Mississippi
# 
# # Output : i = 04 s = 04 p =02 m =01

# In[24]:


def most_frequent(names):
    counts = dict()
    for name in names:
        if name not in counts:
            counts[name] = 1
        else :
            counts[name] = counts[name] + 1
    return(counts)
counts = most_frequent("mississippi")
print(counts)
cnt = sorted(counts.items(),key=lambda x:x[1], reverse = True)
new_dic = dict(cnt)
print(new_dic)

