#####
#
# Les 12 - Make the "Guess the secret number" game more modular
#
# Use functions to make the game more modular. Also try to add another while loop so the user can play
# many rounds of the game without having to re-run the program each time.
#
# You can let the user choose the level of the game: 'Easy' of 'Hard'
# The easy level has suggestions "try something smaller" or "try something bigger"
# The hard level does not have these suggestions, it only tells you if your guess is right or wrong
#
#####


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


# FUNKTIE - Inlezen van de naam van de speler
def lees_naam():
    while True:
        name = input("Wat is Uw naam? ")
        # Empty strings return False!
        if not name:
            print("Naam mag niet leeg zijn. Gelieve opnieuw Uw naam in te voeren.\n")
        else:
            # De lus breken
            break
    return name


# FUNKTIE - Letter inlezen van lijst [mogelijkheden]. Zowel kleine als hoofdletter zijn toegestaan.
def lees_letter(msg_for_user, mogelijkheden):
    while True:
        invoer = input(msg_for_user)
        invoer = invoer.upper()
        if invoer in mogelijkheden:
            # De lus breken
            break
        else:
            print("Dat was geen correct invoer. Probeert U het aub opnieuw...\n")
    return invoer


# FUNKTIE - Toon de huidige top 3 scores
def get_top_scores():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
    # Empty lists return False
    if not score_list:
        print("\nEr zijn nog geen top scores opgeladen!\n")
    else:
        print("\nDe huidige top scores zijn:")

        # Sort the list of dictionaries per attempts and keep only the top 3 best scores
        new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

        # Print the new sorted scores
        for score_dict in new_score_list:
            print("Speler {} had op {} {} poging(en) nodig om het geheim getal {} te raden. Wrong guesses: {}"
                  .format(score_dict.get("speler"), score_dict.get("date"), str(score_dict.get("attempts")),
                          str(score_dict.get("secret")), str(score_dict.get("wrong_guesses"))))
        print()


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
    print("\nDit is het 'Guess the Secret Number' spel!\n")

    # 2. Naam van de speler inlezen
    naam = lees_naam()
    print("Welkom, " + naam + "!\n")

    # 3. Main loop
    while True:
        boodschap = "Would you like to A) play a new game, B) see the best scores, or C) quit? "
        selection = lees_letter(boodschap, ["A", "B", "C"])
        if selection == "A":
            boodschap = "Wil U het (E)asy of (H)ard level? "
            level = lees_letter(boodschap, ["E", "H"])
            if level == "E":
                play_game(naam, "easy")
            else:
                play_game(naam, "hard")
        elif selection == "B":
            get_top_scores()
        else:
            break

    # 4. Afscheid
    print("\nBedankt voor het spelen. Hope to see you soon...")


if __name__ == "__main__":
    main()
