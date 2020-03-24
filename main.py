

amino_acids= {
"A":"Alanine",
"C": "Cysteine",
"D": "Aspartic Acid",
"E":"Glutamic Acid",
"F":"Phenylalanine",
"G":"Glycine",
"H":"Histidine",
"I":"Isoleucine",
"K":"Lysine",
"L":"Leucine",
"M":"Methionine",
"N":"Asparagine",
"P":"Proline",
"Q":"Glutamine",
"R":"Arginine",
"S":"Serine",
"T":"Threonine",
"V":"Valine",
"W":"Tryptophan",
"Y":"Tyrosine"
}

codons = {
"GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A",
"UGC":"C","UGU":"C",
"GAC":"D","GAU":"D",
"GAA":"E","GAG":"E",
"UUC":"F","UUU":"F",
"GGA":"G","GGC":"G","GGG":"G","GGU":"G",
"CAC":"H","CAU":"H",
"AUA":"I","AUC":"I","AUU":"I",
"AAA":"K","AAG":"K",
"UUA":"L","UUG":"L","CUA":"L","CUC":"L","CUG":"L","CUU":"L",
"AUG":"M",
"AAC":"N","AAU":"N",
"CCA":"P","CCC":"P","CCG":"P","CCU":"P",
"CAA":"Q","CAG":"Q",
"AGA":"R","AGG":"R","CGA":"R","CGC":"R","CGG":"R","CGU":"R",
"AGC":"S","AGU":"S","UCA":"S","UCC":"S","UCG":"S","UCU":"S",
"ACA":"T","ACC":"T","ACG":"T","ACU":"T",
"GUA":"V","GUC":"V","GUG":"V","GUU":"V",
"UGG":"W",
"UAC":"Y","UAU":"Y"

}


x=input("Enter your nucleotide code :")
#print("Here's the sequence of amino acids present in it: ")
print("Here's the peptide sequence: ")
keys_list=codons.keys()
#if x in keys_list+
for index_x in range(0,len(x),3) :
	y=codons.get(x[index_x:index_x+3],"NONE")
	if (y == "NONE"):
		print("TERMINATING CODON")
	else:
		print(amino_acids.get(y,"NONE"))
		index_x=index_x + 3
#else 
#	print("CODON DOES NOT CODE FOR ANY AMINO ACID")
	
