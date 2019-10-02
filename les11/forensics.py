#####
# Les 11 - Forensics
#
# There has been a hideous crime! A full container of ice cream was stored in the SmartNinja fridge -
# and now it's completely empty. But the criminal made a fatal mistake. S/he left a spoon inside the
# container and with a spoon also his/her DNA. A perfect case for our CSI investigators!
#
# Raphael --> als 1 eigenschap van een persoon niet in de DNA string staat mag je de loop al skippen
#
#####
'''
# Nodige external packages importeren
import json

# 1. Welcome
print("Dit is het CSI Forensics Icecream onderzoek\n")

# 2. De dna.txt file openen en inlezen als string
with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()
print(dna)

#3. Initialisatie van de variabelen
# Hair color variabelen
black = "CCAGCAATCGC"
brown =  "GCCAGTGCCG"
blonde = "TTAGCTATCGC"

# Facial shape variabelen
square = "GCCACGG"
round = "ACCACAA"
oval = "AGGCCTCA"

# Eye color variabelen
blue = "TTGTGGTGGC"
green = "GGGAGGTGGC"
brown = "AAGTAGTGAC"

# Gender variabelen
female = "TGAAGGACCTTC"
male = "TGCAGGAACTTC"

# Race variabelen
white = "AAAACCTCA"
black = "CGACTACAG"
asian =  "CGCGGGCCG"

# 6. Afscheid
print("\nBedankt voor het gebruiken van onze CSI service. Hope to see you soon...")
'''
for i in range(5):
    print(i, end=", ")
