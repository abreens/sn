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


# De nodige external modules importeren
import random
import json
import datetime


# FUNKTIE - Inlezen van een geheel getal tussen 1 en <upper_limit>
def lees_geheel(upper_limit):
    while True:
        invoer = input("\nGeef een getal (tussen 1 en " + str(upper_limit) + "): ")
        try:
            getal = int(invoer)
        except ValueError:
            print("Jammer genoeg was dit geen (geheel) getal. Probeer aub opnieuw...")
        else:
            if 1 <= getal <= upper_limit:
                # De lus breken
                break
            else:
                print("Het getal moet tussen 1 en " + str(upper_limit) + " liggen. Probeer aub opnieuw...")
    return getal


# FUNKTIE - Speel het spel
def play_game(name, lvl):
    # Initialisaties
    secret = random.randint(1, 30)
    attempts = 0
    dts = str(datetime.datetime.now())  # dts = Date Time Stamp
    wrong_guesses = []

    # De score file openen en inlezen
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())

    # Boodschap voor de gebruiker
    print("\nHET SPEL START NU!")

    # Main game loop
    while True:
        guess = lees_geheel(30)
        attempts += 1

        # Het antwoord analyseren
        if guess == secret:
            print("\nYou've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            print("Dit waren Uw verkeerde keuzes: ", wrong_guesses)
            print()

            # De score_list.txt file updaten en wegschrijven
            score_list.append({"attempts": attempts, "date": dts, "speler": name, "secret": secret,
                               "wrong_guesses": wrong_guesses})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
            # De lus breken
            break

        else:
            # Het getal werd niet geraden.
            print("Sorry, Uw gok is niet correct...")
            if lvl == "easy":
                # Een tip voor de gebruiker meegeven als mode 'Easy' is
                if guess > secret:
                    print("Tip: try something smaller")
                else:
                    print("Tip: try something bigger")
        # De huidige guess dynamisch opslaan in lijst wrong_guesses
        wrong_guesses.append(guess)


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
                play_game(naam, "easy")
            else:
                play_game(naam, "hard")
        elif selection == "B":
            f.druk_topscores()
        else:
            break

    # 4. Afscheid
    print("\nBedankt voor het spelen. Hope to see you soon...")


if __name__ == "__main__":
    main()
