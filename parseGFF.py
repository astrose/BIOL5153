import argparse
import csv
from Bio import Se2qIO

#create variable parser
parser=argparse.ArgumentParser(description=This script parses GFF files, and will do more later")

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
