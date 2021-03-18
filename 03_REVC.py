# dna = "AAAACCCGGT"

dna = input('Enter your DNA seq: ')

def reverse_complementary(dna):
    dna_complement = ""
    for base in dna:
        if base == "A":
            dna_complement += "T"
        if base == "T":
            dna_complement += "A"
        if base == "G":
            dna_complement += "C"
        if base == "C":
            dna_complement += "G"
    return dna_complement[::-1]


print("Reverse Complementary Strand", reverse_complementary(dna), sep = '\n')
