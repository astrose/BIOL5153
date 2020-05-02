#! bin/bash env python

import os
import sys

#Q1, Binning DNA sequences 
# go through and process all files that end in .dna
for file in os.listdir("."):
	if file.endswith(".dna"):
		print("reading sequences from " + file_name)
		dna_file = open(file_name)
		# for each line, calculate the sequence length
		for line in dna_file:
			dna = line.rstrip("\n")
			length = len(dna)
			print("sequence length is " + str(length))
			# figure out which bin the sequence belongs in
			for bin_lower in range(100,1000,100):
				bin_upper = bin_lower + 99
				if length >= bin_lower and length < bin_upper:
				# once we know the correct bin, write out the sequence
				print("bin is " + str(bin_lower) + " to " + str(bin_upper))
				bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
				output_path = bin_folder_name + '/' + str(seq_number) + '.dna'
				output = open(output_path, "w")
				output.write(dna)
				output.close()
				# increment the sequence number
				seq_number = seq_number+1

#Q2 Kmer counting

# convert command line arguments to variables
kmer_size = int(sys.argv[1])
count_cutoff = int(sys.argv[2])
# define the function to split dna
def split_dna(dna, kmer_size):
	kmers = []
	for start in range(0,len(dna)-(kmer_size-1),1):
		kmer = dna[start:start+kmer_size]
		kmers.append(kmer)
	return kmers

# create an empty dictionary to hold the counts
kmer_counts = {}
# process each file with the right name
for file_name in os.listdir("."):
	if file_name.endswith(".dna"):
		dna_file = open(file_name)
		# process each DNA sequence in a file
		for line in dna_file:
			dna = line.rstrip("\n")
			# increase the count for each k-mer that we find
			for kmer in split_dna(dna, kmer_size):
				current_count = kmer_counts.get(kmer, 0)
				new_count = current_count + 1
				kmer_counts[kmer] = new_count
# print k-mers whose counts are above the cutoff
for kmer, count in kmer_counts.items():
	if count > count_cutoff:
		print(kmer+ " : " + str(count))

