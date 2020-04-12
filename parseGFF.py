# /usr/bin/env python3
import argparse
import csv
from Bio import SeqIO

#create variable parser
parser=argparse.ArgumentParser("description=This script parses GFF files, and will do more later")

#add positional arguments
parser.add_argument("gff", help="name of the GFF file")
parser.add_argument("fasta", help="name of the FASTA file")

#parsethe arguments
args = parser.parse_args()

#read and parse the FASTA file
genome=SeqIO.read(args.fasta, "fasta")

#read GFFfile, line by line
with open(args.gff, "r") as gff_file:
	reader = csv.reader(gff_file, delimiter="\t")
	for line in reader:
		#skip blank lines
		if not line:
			continue
		else:
			start= line [3]
			end  = line [4]
			pint(start, end)
			

#list gene names
gene_names = []

#set input file
with open (args.gff,"r") as gff_file:
	with open(args.fasta, "r") as fasta_file:
		reader=csv.reader(gff_file, delimiter="\t")
	
	#extract CDS
	for line in reader:
		if not line:
			continue

		else:
			if (line[2]=="CDS"):
				start=int(line[3])
				end= int(line[4])
				gene_list.append(genome.seq[start:end])

#create function to calculate and print the GC content of gene_list to 1 decimal place
def get_gc_content(gene_list, sig_figs=1):
	length= len(gene_list):
	#count the amount and G's and C's
	g_count = gene_list.upper().count("G")
	c_count = gene_list.upper().count("C")
	#get average, return how much is present
	gc_content =(g_count + c_count)/length
	return(gc_content, sig_figs)

#for every line in gene_list, print the gc content
for i in gene_list:
	print("The GC content is " + str(get_gc_content(i)))

#close file
gff_file.close()
fasta_file.close()

