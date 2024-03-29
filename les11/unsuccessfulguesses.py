#####
#
# Les 11 - Add unsuccessful guesses
#
# Every good game needs to store the best score, so that you can try to best it.
#
# During the game, collect user's unsuccessful guesses and then store them in the dictionary
# under the name "wrong_guesses". Hint: you can store a list in a dictionary. ;)
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
        print("De huidige top scores zijn:")
        for score_dict in score_list:
            print("On " + score_dict.get("date") + ", player " + score_dict.get("speler") + " needed " +
                  str(score_dict.get("attempts")) + " attempts to guess the secret number " +
                  str(score_dict.get("secret")) + ". Wrong guesses were: " + str(score_dict.get("wrong_guesses")))

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
