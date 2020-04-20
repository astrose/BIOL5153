#!/usr/bin/env python
# coding: utf-8

# In[2]:


cat=open("wheres_katharine.txt").read().rstrip("\n")


# In[34]:


print(cat)


# In[35]:


import re


# In[144]:


#Construct a regular expression to find all instances of the name Katharine in “The concert” short story
Katherine= "(c|k)(ath)+(a|e)*r+(i|y)n+e*"
#capture all Katherine's, print name and position and length
for match in re.finditer(pattern,concert,re.I):
    start = match.start()
    end = match.end()
    length = end-start
    print(match.group() + " is " + str(length) + " letters long and " "starts at position: " + str(start) + " and ends at: " + str(end) + ".")


# In[159]:


for match in re.finditer(pattern,concert,re.I):
    start = match.start()
    end = match.end()
    length = end-start
    print("\t" match.group() + str(length) + str(start)+ str(end))


# 

# In[160]:


#Print the following output in a small tab-delimited table with these columns:

