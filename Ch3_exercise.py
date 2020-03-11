#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Q1, Splitting genomic DNA
#open genomic DNA file
my_gen_dna=open("genomic_dna.txt")
my_dna=my_gen_dna.read()


# In[13]:


#open coding file to write to
coding_file=open("coding_dna.txt", "w")
#open noncoding file to write to
noncoding_file=open("noncoding_dna.txt", "w")


# In[14]:


#extract DNA for coding and noncoding regions (chapter 2)
exon1=my_dna[0:62]
exon2=my_dna[90:1000]
intron=my_dna[60:90]


# In[15]:


#actually write information to these files
coding_file.write(exon1+ exon2)
#From Question 2, DNA breakdown 
noncoding_file.write(intron)


# In[28]:


#Q2, Writing a FASTA File
#create output file
output=open("dna_seq.fasta", "w")


# In[29]:


#create header variables
header_1="ABC123"
header_2="DEF456"
header_3="HIJ789"
#create sequence variables
seq1="ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq2="actgatcgacgatcgatcgatcacgact"
seq3="ACTGAC-ACTGT--ACTGTA----CATGTG"


# In[30]:


output.write(">"+ header_1 + "\n" + seq1 + "\n")
output.write(">" + header_2 + "\n" + seq2.upper() + "\n")
output.write(">" + header_3 + "\n" + seq3.replace("-","") + "\n")


# In[31]:


#q3, Writing multiple FASTA files
output_1=open(header_1+".fasta", "w")
output_2=open(header_2+".fasta", "w")
output_3=open(header_3+".fasta", "w")


# In[32]:


#write 50 multiple files
output_1.write(">"+ header_1 + "\n" + seq1 + "\n")
output_2.write(">" + header_2 + "\n" + seq2.upper() + "\n")
output_3.write(">" + header_3 + "\n" + seq3.replace("-","") + "\n")


# In[ ]:




