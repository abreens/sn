#####
# Les 11 - Forensics
#
# There has been a hideous crime! A full container of ice cream was stored in the SmartNinja fridge -
# and now it's completely empty. But the criminal made a fatal mistake. S/he left a spoon inside the
# container and with a spoon also his/her DNA. A perfect case for our CSI investigators!
#
#####

# 1. WELCOME
print("Dit is het CSI Forensics Icecream onderzoek\n")

# 2. DE DNA.TXT FILE INLEZEN
with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

# 3. INITIALISATIE VAN DE VARIABELEN
# 3.1 Hair color variabelen
black_hair = "CCAGCAATCGC"
brown_hair = "GCCAGTGCCG"
blonde = "TTAGCTATCGC"

# 3.2 Facial shape variabelen
square = "GCCACGG"
round_face = "ACCACAA"
oval = "AGGCCTCA"

# 3.3 Eye color variabelen
blue = "TTGTGGTGGC"
green = "GGGAGGTGGC"
brown_eyes = "AAGTAGTGAC"

# 3.4 Gender variabelen
female = "TGAAGGACCTTC"
male = "TGCAGGAACTTC"

# 3.5 Race variabelen
white = "AAAACCTCA"
black_race = "CGACTACAG"
asian = "CGCGGGCCG"

# 4. DE LIJST MET VERDACHTEN SAMENSTELLEN
verdachten = [{"name": "Eva", "gender": female, "race": white, "hair": blonde, "eye": blue, "face": oval},
              {"name": "Larisa", "gender": female, "race": white, "hair": brown_hair, "eye": brown_eyes, "face": oval},
              {"name": "Matej", "gender": male, "race": white, "hair": black_hair, "eye": blue, "face": oval},
              {"name": "Miha", "gender": male, "race": white, "hair": brown_hair, "eye": green, "face": square}]

# 5. HET ONDERZOEK
print("Analysing...\n")

dader = ""
meeste = 0
for i in verdachten:
    match = 0
    if i["gender"] in dna:
        match += 1
    if i["race"] in dna:
        match += 1
    if i["hair"] in dna:
        match += 1
    if i["eye"] in dna:
        match += 1
    if i["face"] in dna:
        match += 1

    # Tussentijds resultaat afdrukken
    print("{} heeft {} overeenkomst(en) in de DNA file".format(i["name"], match))

    # De dader is diegene met het meeste matches
    if match > meeste:
        meeste = match
        dader = i["name"]

# Het resultaat van de anylyse afdrukken
print("\n" + dader.upper() + " is de dader met " + str(meeste) + " matches in de DNA file!")

# 6. Afscheid
print("\nBedankt voor het gebruiken van onze CSI service. Hope to see you soon...")
