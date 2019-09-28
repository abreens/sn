#####
# Les 9 - DE SMARTNINJA UNIT CONVERTER
#
# Create a program that converts units. More specifically, kilometers into miles.
#
# Plan:
# 1. The program greets user and describes what's the purpose of the program.
# 2. The program asks user to enter number of kilometers.
# 3. User enters the amount of kilometers.
# 4. The program converts these kilometers into miles and prints them.
# 5. The program asks user if s/he'd want to do another conversion.
# 6. If yes, repeat the above process (except the greeting).
# 7. If not, the program says goodbye and stops.
#
#####

# FUNKTIE - Lees een (decimaal) getal
def lees_getal():
    while True:
        # 3. Kilometers inlezen
        invoer = input("\nGeef een getal als kilometers aub (gebruik een . om een decimaal getal in te voeren!): ")
        try:
            getal = float(invoer)
        except:
            print("Dat was geen correcte invoer. Probeer aub opnieuw...")
        else:
            print("Dit was een correcte invoer. Dank U wel!\n")
            # De lus breken
            break
    return (getal)

# Initialisaties
factor = 0.62138818119679

# 1. Greeting and doel uitleggen
print("Welkom bij de SmartNinja Unit Convertor.")
print("Dit programma zal ingevoerde kilometers omzetten naar mijlen.")
print("Veel plezier!")

while True:
    # 2. Inlezen van de kilometers
    kilometers = lees_getal()

    # 4. Omzetten naar miles en het resultaat afdrukken
    print(str(kilometers) + " km is gelijk aan " + str(kilometers * factor) + " miles.\n")

    # 5. Vraag of de gebruiker nog een convertie wil doen
    invoer = input("Wil U nog een convertie doen (j/n)? ")

    # 6. Enkel "n" zal het programma stoppen. Bij elke andere invoer doen we het gewoon nog eens ;)
    if invoer.lower() == "n":
        break

# 7. Afscheid
print("\nBedankt voor het gebruiken van onze Converter Service. Tot ziens!")