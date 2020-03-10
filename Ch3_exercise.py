#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Q1, Processing DNA in a file
#open file to work with
file=open("input.txt")


# In[15]:


#creat an output file to write to
output=open("trimmed_input.txt","w")


# In[23]:


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
    print("The length of this DNA is " + str(length_dna) +("."))


# In[86]:


#Q2, Multiple exons from genomic DNA
#open genimic file
genomic_dna=open("genomic_dna.txt").read()
#source exon file
exon_data=open("exons.txt")


# In[87]:


#View all lines of the file, commented out code so it would not affect the running of other lines
#for lines in exon_data:
    #print(lines)


# In[88]:


#Split lines propery
for lines in exon_data:
    #Split exon into readable elements
    exon_split=lines.split(',')
    #create a start placement with first element in the line
    start= int(exon_split[0])
    #create stop placement with the first element (reading from the back) which is the last element essentially
    stop= int(exon_split[-1])
    #extraxt exon from genomic data, append to end of sequence
    exon=genomic_dna[start:stop]
    coding_sequence= "" + exon
    print("The coing sequence is:" + coding_sequence)


# In[91]:


#Wtite sequence to output
output=open("coding_sequence.txt","w")
output.write(coding_sequence)
output.close()    


# In[ ]:





# In[ ]:




