#####
# Les 11 - Add some more data in the dictionary
#
# Every good game needs to store the best score, so that you can try to best it.
#
# For now our 'Guess the secret number' game only stores the number of attempts and the date.
# Let's also store the name of the player and the secret number in each game.
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

# 2. Naam van de speler inlezen
naam = lees_naam()

# 3. Welcome
print("Welkom bij het 'Guess the Secret Number' spel, " + naam + "!\n")

# 4. De huidige top scores uitlezen en afdrukken
print("De huidige top scores zijn:")
with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    # Empty lists return False
    if not score_list:
        print('Er zijn nog geen Top scores beschikbaar!')
    else:
        for score_dict in score_list:
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date") + ", speler: "
                  + score_dict.get("speler") + ", secret: " + str(score_dict["secret"]))

# 5. Een geheim getal tussen 1 en 30 raden
while True:
    guess = lees_geheel()
    attempts += 1

    # Het antwoord analyseren
    if guess == secret:
        print("\nYou've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        # Het aantal pogingen toevoegen aan de score_list.txt file
        score_list.append({"attempts": attempts, "date": dts, "speler": naam, "secret": secret})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        # De lus breken
        break

    # Het getal werd niet geraden. Tips voor de speler meegeven.
    elif guess > secret:
        print("Sorry, your guess is not correct... Try something smaller")
    else:
        print("Sorry, your guess is not correct... Try something bigger")

# 6. Afscheid
print("\nBedankt voor het spelen. Hope to see you soon...")
