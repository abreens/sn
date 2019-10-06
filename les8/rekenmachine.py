#####
# Les 8 - DE SMARTNINJA REKENMACHINE
#
# Write a program that does the basic arithmetic operations: addition (+), subtraction (-), # multiplication (*),
# and division (/). Ask the user to enter two numbers and the arithmetic operation ("+", "-", "*" or "/").
#
#####


# FUNKTIE - LEES EEN GETAL ("g") OF EEN OPERATOR ("o")
def lees(soort, omschrijving):
    if soort == "g":
        # Een GETAL inlezen en kontroleren
        notok = True
        while notok:
            invoer = input("Geef een geheel " + omschrijving + " aub: ")
            try:
                getal = int(invoer)
            except ValueError:
                print("Jammer genoeg was dit geen (geheel) getal. Probeer aub opnieuw...\n")
            else:
                print("Dit was een correcte invoer. Dank U wel!\n")
                # De lus breken
                notok = False
        return getal
    else:
        # Een OPERATOR inlezen en kontroleren
        operatoren = ["+", "-", "*", "/"]
        invoer = ""
        while invoer not in operatoren:
            invoer = input("Geef een operator aub ('+' of '-' of '*' of '/'): ")
            if invoer in operatoren:
                print("Dit was een correcte operator. Proficiat!\n")
            else:
                print("Jammer genoeg was dit geen correcte operator. Probeer aub opnieuw...\n")
        return invoer


# FUNKTIE - RESULTAAT BEREKENEN
def resultaat(i, j, o):
    if o == "+":
        return i + j
    elif o == "-":
        return i - j
    elif o == "*":
        return i * j
    elif o == "/":
        if j == 0:
            return "DIV BY ZERO ERROR!!!"
        else:
            return i / j


# TITEL AFDRUKKEN
print("LES 8 - DE SMARTNINJA REKENMACHINE\n")

# INLEZEN VAN DE TWEE GETALLEN
getal1 = lees("g", "getal 1")
getal2 = lees("g", "getal 2")

# DE INGEVOERDE GETALLEN EVEN AFDRUKKEN - JUST FOR FUN ;)
print("Getal 1 was: ", getal1)
print("Getal 2 was: ", getal2)
print("\n")

# INLEZEN VAN DE OPERATOR. DE TWEEDE PARAMETER HEEFT HIER GEEN EFFECT.
# DE EERSTE OOK NIET EIGENLIJK ZOLANG DIE MAAR NIET "g" IS ;)
operator = lees("o", "")

# DE INGEVOERDE OPERATOR AFDRUKKEN - OOK WEER JUST FOR FUN ;)
print("De ingevoerde operator was: " + operator + "\n")

# DOE DE BEREKENING EN DRUK HET RESULTAAT AF
uitkomst = str(resultaat(getal1, getal2, operator))
# Het resultaat wordt op verschillende manieren afgedrukt
print("Het resultaat is...")
print(str(getal1) + " " + operator + " " + str(getal2) + " = " + uitkomst)
print(str(getal1), operator, str(getal2), "=", uitkomst)
print("{} {} {} = {}".format(getal1, operator, getal2, uitkomst))
print("%s %s %s = %s" % (getal1, operator, getal2, uitkomst))

# AFSCHEID
print("\nBedankt voor het gebruiken van onze RM service. Tot ziens!")
