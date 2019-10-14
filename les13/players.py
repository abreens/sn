#####
#
# Les 13 - OOP Players
#
# Let's make our program for basketball and football players a bit more useful. Add an option that a user can
# enter data (via input()) and at the end of the program the data gets saved in a text file.
#
# Hint: you can easily convert an object into a dictionary via the in-built __dict__ method.
# Try this in your program: lebron.__dict__ (note that there are 2 underscores on each side).
#
# Use the knowledge that you gained while building the Guess the secret number game.
#
#####

# Gezamelijke funkties importeren
import functions as f


def main():

    # 1. Welcome
    f.say_hello("Welkom bij het Spelers Management programma")

    # 2. Hoofd loop
    while True:
        boodschap = '\nWil U A) een speler toevoegen, B) de geregistreerde spelers bekijken of C) stoppen? '
        selection = f.lees_letter(boodschap, ["A", "B", "C"])

        if selection == "A":
            # Een speler toevoegen
            boodschap = "\nWil U een (B)asketbal speler of een (V)oetbal speler toevoegen? "
            keuze = f.lees_letter(boodschap, ["B", "V"])
            nieuwe_speler = f.create_speler(keuze)

            # Opslaan?
            print("\nU hebt de volgende speler gedefinieerd: ")
            print(nieuwe_speler.__dict__)
            boodschap = "\nWil U deze speler opslaan? (J/N) "
            keuze = f.lees_letter(boodschap, ["J", "N"])
            if keuze == "J":
                # De speler opslaan in de database
                f.schrijf_db("spelers.txt", nieuwe_speler.__dict__)
            elif keuze == "N":
                print("De gegevens van de speler worden niet opgeslagen!")

        elif selection == "B":
            # Bestaande spelers afdrukken
            f.druk_records("spelers.txt")

        elif selection == "C":
            # Stoppen
            break

    # 3. Afscheid
    print("\nBedankt voor het gebruik van onze service. Hope to see you soon...")


if __name__ == "__main__":
    main()
