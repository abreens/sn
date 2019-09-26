#####
# Les 8 - DE SMARTNINJA REKENMACHINE
#
# Write a program that does the basic arithmetic operations: addition (+), subtraction (-), # multiplication (*),
# and division (/). Ask the user to enter two numbers and the arithmetic operation ("+", "-", "*" or "/").
#
#####

# FUNKTIE - LEES GETAL
def lees_getal(omschrijving):
    notOK = True
    while notOK:
        invoer = input("Geef " + omschrijving + " aub: ")
        if invoer.isdigit():
            print("Dit was een getal. Proficiat!\n")
            notOK = False
        else:
            print("Jammer genoeg was dit geen getal. Probeer aub opnieuw...\n")
    return int(invoer)

# FUNKTIE - LEES OPERATOR
def lees_operator():
    invoer = "een_duveltje"
    while (invoer not in operatoren):
        invoer = input("Geef een operator aub: ")
        if (invoer in operatoren):
            print("Dit was een correcte operator. Proficiat!\n")
        else:
            print("Jammer genoeg was dit geen correcte operator. Probeer aub opnieuw...\n")
    return (invoer)

# FUNKTIE - RESULTAAT BEREKENEN
def resultaat (i, j, o):
    if o == "+":
        return i + j
    elif o == "-":
        return i - j
    elif o == "*":
        return i * j
    elif o == "/":
        return i / j

# INITIALISATIES
operatoren = ["+", "-", "*", "/"]

# TITEL AFDRUKKEN
print("LES 8 - DE SMARTNINJA REKENMACHINE\n")

# INLEZEN VAN DE TWEE GETALLEN
getal1 = lees_getal("getal 1")
getal2 = lees_getal("getal_2")

# DE INGEVOERDE GETALLEN AFDRUKKEN
print("Getal 1 was: ", getal1)
print("Getal 2 was: ", getal2)
print("\n")

# INLEZEN VAN DE OPERATOR
operator = lees_operator()

# DE INGEVOERDE OPERATOR AFDRUKKEN
print("De ingevoerde operator was: " + operator + "\n")

# DE BEREKENING UITVOEREN
print(getal1, " ", operator, " ", getal2, " = ", resultaat(getal1, getal2, operator))