#####
#
# Les 13 - Model for the "Guess the secret number" results
#
# Design your "Guess the secret number" game in a way that every result will be stored as an object.
# Create a model called Result, that takes the following data:
#    score
#    player_name
#    date
# Then save the objects into a results.txt file (use the __dict__ method, like in the previous homework).
#
#####


# Gezamelijke funkties importeren
import functions as f


def main():
    # 1. Welcome
    f.say_hello("Welkom bij het 'Guess the Secret Number' spel")

    # 2. Naam van de speler inlezen
    boodschap = "Wat is Uw naam? "
    naam = f.lees_str(boodschap)
    print("Welkom, " + naam + "!")

    # 3. Main loop
    while True:
        boodschap = "\nWould you like to A) play a new game, B) see the best scores, or C) quit? "
        selection = f.lees_letter(boodschap, ["A", "B", "C"])
        if selection == "A":
            boodschap = "\nWil U het (E)asy of (H)ard level? "
            level = f.lees_letter(boodschap, ["E", "H"])
            if level == "E":
                f.play_game(naam, "easy")
            else:
                f.play_game(naam, "hard")
        elif selection == "B":
            f.druk_topscores()
        else:
            break

    # 4. Afscheid
    print("\nBedankt voor het spelen. Hope to see you soon...")


if __name__ == "__main__":
    main()