#!/usr/bin/env python
# coding: utf-8

# In[14]:


#open file to work with
file=open("input.txt")


# In[15]:


#creat an output file to write to
output=open("trimmed_input.txt","w")


# In[17]:


#create for loop to read file line by line
#for each line in this file
for line in file:
    #get the length of it
    length_dna= len(line)
    #give me lines 14 to the end of line
    cut_dna=line[14:length_dna]
    #write out the trimmed sequence
    output.write(cut_dna)
    #print out the cute DNA with its length
    print(cut_dna)
    print(length_dna)

