filename= "dna.txt"
infile= open(filename, "r")
dna_sequence=infile.read()
infile.close

print(dna_sequence)
length=(len(dna_sequence))
# print(length)

#Percentages of all capital letters

a_percent= (dna_sequence.count('A')/length *100)
print("a_percent: ", end='')
print(round(a_percent,2))

g_percent= (dna_sequence.count('G')/length *100)
print("g_percent: ", end='')
print(round(g_percent,2))


c_percent= (dna_sequence.count('C')/length *100)
print("c_percent: ", end='')
print(round(c_percent,2))

t_percent= (dna_sequence.count('T')/length *100)
print("t_percent: ", end='')
print(round(t_percent,2))

#Change to lowercase and run
infile= open(filename, "r")
lowercase_dna=infile.read()
infile.close

lowercase_dna = dna_sequence.lower()
print(lowercase_dna)
'A'=='a'
'C'=='c'
'T'=='t'
'G'=='g'

a_lpercent= (lowercase_dna.count('A')/length *100)
print("a_lpercent: ", end='')
print(round(a_lpercent,2))

g_lpercent= (lowercase_dna.count('G')/length *100)
print("g_percent: ", end='')
print(round(g_lpercent,2))


c_lpercent= (lowercase_dna.count('C')/length *100)
print("c_percent: ", end='')
print(round(c_lpercent,2))

t_lpercent= (lowercase_dna.count('T')/length *100)
print("t_percent: ", end='')
print(round(t_lpercent,2))
