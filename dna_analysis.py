# DNA Sequence Analysis
# Author: Akshat Vishwakarma

dna = "ATGCGTACGTTAGC"

# Validate DNA sequence
valid_bases = "ATGC"

if all(base in valid_bases for base in dna):
    print("Valid DNA sequence")
else:
    print("Invalid DNA sequence")

# Nucleotide composition
for base in valid_bases:
    print(base, ":", dna.count(base))

# GC content
gc_content = (dna.count("G") + dna.count("C")) / len(dna) * 100
print("GC Content:", round(gc_content, 2), "%")

# Reverse sequence
print("Reverse sequence:", dna[::-1])

# Last 6 nucleotides
print("Last 6 nucleotides:", dna[-6:])
