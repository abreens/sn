#####
# Les 11 - Print out only the top 3 results
#
# Now that we removed the score_list.sort() line (because it doesn't work with dictionaries in the list),
# we have to find another way to sort the scores. There are many ways how to do it. Use your imagination
# (and Google) and try to figure out at least one of them. :)
#####

# Nodige external packages importeren
import random
import json
import datetime


# FUNKTIE - Inlezen van een geheel getal tussen 1 en 30
def lees_geheel():
    while True:
        invoer = input("\nGuess the secret number (between 1 and 30): ")
        try:
            getal = int(invoer)
        except ValueError:
            print("Jammer genoeg was dit geen (geheel) getal. Probeer aub opnieuw...")
        else:
            if 1 <= getal <= 30:
                print("Dit was een correcte invoer! Wij analyseren nu het resultaat...")
                # De lus breken
                break
            else:
                print("Het getal moet tussen 1 en 30 liggen. Probeer aub opnieuw...")
    return getal


# FUNKTIE - Inlezen van de naam van de speler
def lees_naam():
    while True:
        name = input("Wat is Uw naam? ")
        # Empty strings return False!
        if not name:
            print("Naam mag niet leeg zijn. Gelieve opnieuw Uw naam in te voeren.\n")
        else:
            print("Dat was een correcte invoer. We gaan verder met het spel...\n")
            # De lus breken
            break
    return name


# 1. Initialisaties
secret = random.randint(1, 30)
attempts = 0
dts = str(datetime.datetime.now())  # dts = Date Time Stamp
wrong_guesses = []

# 2. Welcome
print("Dit is het 'Guess the Secret Number' spel!\n")

# 3. Naam van de speler inlezen
naam = lees_naam()
print("Welkom, " + naam + "!\n")

# 4. De huidige top scores uitlezen en afdrukken
with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    # Empty lists return False
    if not score_list:
        print("Er zijn nog geen top scores opgeladen!")
    else:
        print("De top scores zijn:")

        # Sort the list of dictionaries per attempts and keep only the top 3 best scores
        new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

        # Print the new sorted scores
        for score_dict in new_score_list:
            print("Speler {} had op {} {} pogingen nodig om het geheim getal {} te raden. Wrong guesses: {}".format(
                score_dict.get("speler"),
                score_dict.get("date"),
                str(score_dict.get("attempts")),
                str(score_dict.get("secret")),
                str(score_dict.get("wrong_guesses"))
            ))

# 5. Een geheim getal tussen 1 en 30 raden
while True:
    guess = lees_geheel()
    attempts += 1

    # Het antwoord analyseren
    if guess == secret:
        print("\nYou've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        print("Dit waren Uw verkeerde keuzes: ", wrong_guesses)

        # De score_list.txt file updaten en wegschrijven
        score_list.append({"attempts": attempts, "date": dts, "speler": naam, "secret": secret,
                           "wrong_guesses": wrong_guesses})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        # De lus breken
        break

    # Het getal werd niet geraden. Tips voor de speler meegeven.
    elif guess > secret:
        print("Sorry, your guess is not correct... Try something smaller")
    else:
        print("Sorry, your guess is not correct... Try something bigger")

    # De huidige guess dynamisch opslaan in lijst wrong_guesses
    wrong_guesses.append(guess)

# 6. Afscheid
print("\nBedankt voor het spelen. Hope to see you soon...")
