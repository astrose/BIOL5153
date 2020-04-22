#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Q1 Function with two arguments, returns percentage of aa in protein
#Testing out the argument before putting into a function
dna = "MSRSLLLRFLLFLLLLPPLP"
aa = "R"
aa_count = dna.count(aa)
dna_length = len(dna)
percentage = aa_count * 100 / dna_length
print(percentage)


# In[33]:


def get_aa_percentage(dna, aa):
    #convert dna to uppercase
    dna = dna.upper()
    #convert amino acid to uppercase
    aa = aa.upper()
    aa_count = dna.count(aa)
    dna_length = len(dna)
    #get percentage
    percentage = aa_count * 100 / dna_length
    return percentage


# In[28]:


#Q2 Modify 1st function to take a list of amino acids
def get_aa_percentage(dna, aa_list=['A','I','L','M','F','W','Y','V']):
    dna = protein.upper()
    dna_length = len(protein)
    total = 0
    #create for loop, for every aa in the aa list, count how many of it an get total.
    for aa in aa_list:
        aa = aa.upper()
        aa_count = dna.count(aa)
        total = total + aa_count
    #get percentage of each
    percentage = total * 100 / dna_length
    return percentage

