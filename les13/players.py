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

# Classes importeren
from les13.functions import BasketballPlayer, FootballPlayer


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

            print("\nU hebt de volgende speler gedefinieerd: ")
            print(nieuwe_speler.__dict__)
            print()
            print(nieuwe_speler.last_name)
            print(nieuwe_speler.first_name)

        elif selection == "B":
            # Bestaande spelers afdrukken
            print("\nDe geregistreerde spelers worden opgehaald...\n")
            f.lees_spelers()

        else:
            # Stoppen
            break

    # 3. Afscheid
    print("\nBedankt voor het gebruik van onze service. Hope to see you soon...\n")


    ### PLAYGROUND TO BE DELETED WHEN DONE

    kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", sport="Basketbal", height_cm=210,
                               weight_kg=108, points=27.2, rebounds=7.1, assists=4)

    print(kev_dur.last_name)
    print(kev_dur.rebounds)
    print(kev_dur.weight_to_lbs())
    print()
    print(kev_dur.__dict__)
    print()

    messi = FootballPlayer(first_name="Lionel", last_name="Messi", sport="Voetbal", height_cm=170,
                           weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

    print(messi.first_name)
    print(messi.goals)
    print(messi.weight_to_lbs())
    print()

    print(messi.__dict__)

    ### END OF PLAYGROUND


if __name__ == "__main__":
    main()
