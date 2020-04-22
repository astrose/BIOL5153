#set DNA variable
dna = "ATGTTCGGT"
codon1 = dna[0:3]
codon2 = dna[3:6]
codon3 = dna[6:9]

#View chunks of DNA
print(codon1, codon2, codon3)

#calculate the start position for the final codon
last_codon_start = len(dna) - 2

#process the dna sequence in three base chunks

for start in range(0,last_codon_start,3):
	codon=dna[start:start+3]
	print("one codon is " + codon)
