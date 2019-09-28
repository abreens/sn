#####
# Les 10 - Storing data into a file
#
# Every good game needs to store the best score, so that you can try to best it.
#
# In the case of the "Guess the secret number" game, we'd like to store the number of attempts
# we needed to guess the number. Did we need 6 attempts? Maybe 4? Or even only 2? The lower the number, the better!
#
#####

import random

# FUNKTIE - Inlezen van een geheel getal tussen 1 en 30
def leesgeheel():
    while True:
        invoer = input("\nGuess the secret number (between 1 and 30): ")
        try:
            getal = int(invoer)
        except ValueError:
            print("Jammer genoeg was dit geen (geheel) getal. Probeer aub opnieuw...")
        else:
            if getal >= 1 and getal <= 30:
                print("Dit was een correcte invoer! Wij analyseren nu het resultaat...")
                # De lus breken
                break
            else:
                print("Het getal moet tussen 1 en 30 liggen. Probeer aub opnieuw...")
    return (getal)

# 1. Initialisaties
secret = random.randint(1, 30)
attempts = 0

# 2. Welcome
print("Welkom bij het 'Guess the Secret Number' spel")

# 3. De huidige top score uitlezen en afdrukken
with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Huidige Top Score (attempts): " + str(best_score))

# 4. Een geheim getal tussen 1 en 30 raden
while True:
    guess = leesgeheel()
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        # Aantal pogingen wegschrijven wanneer de topscore werd verbroken
        if attempts < best_score:
            print("PROFICIAT! U HEBT DE TOP SCORE VERBETERD!")
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        # De lus breken
        break

    elif guess > secret:
        print("Sorry, your guess is not correct... Try something smaller")

    elif guess < secret:
        print("Sorry, your guess is not correct... Try something bigger")

