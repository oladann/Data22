def dna_count(dna):

    counter_A = 0
    counter_T = 0
    counter_C = 0
    counter_G = 0

    for nucleotide in dna:
        if nucleotide == "A":
            counter_A += 1
        elif nucleotide == "T":
            counter_T += 1
        elif nucleotide == "C":
            counter_C += 1
        elif nucleotide == "G":
            counter_G += 1

    return print(f"A:{counter_A} T:{counter_T} C:{counter_C} G:{counter_G}")

DNA_CHAIN = "AAAAAAAATTTCCG"
dna_count(DNA_CHAIN)






