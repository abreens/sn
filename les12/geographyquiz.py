#####
#
# Les 12 - Geography Quiz
#
# A local gaming company contacted you to build a game for them. It is a simple geography quiz where a user
# has to guess the capital city of some country:
# > Game: What is the capital city of Slovenia?
# User: Ljubljana
# > Game: This is correct!
#
# Hint: Use a dictionary to create a pool of countries and their capitals:
# countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Slovenia": "Ljubljana"}
#
#####


# De nodige externe modules importeren
import random


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


# FUNKTIE - Het spel spelen
def speel_quiz(dict_capitals, aantal_pogingen):

    print('\nU hebt {} poging(en). Success!'.format(aantal_pogingen))

    # Een willekeurig land en hoofdstad selekteren uit dict_capitals
    land, hoofdstad = random.choice(list(dict_capitals.items()))
    print('\nWat is de hoofdstad van {}?'.format(land))

    i = 1
    while i <= aantal_pogingen:

        # Een gok inlezen
        guess = None
        while not guess:
            guess = input('\nPoging {}: '.format(i))
            if not guess:
                print("Gelieve iets in te voeren...")

        # Controleren of het antwoord juist is
        if guess == hoofdstad:
            print("Congratulations! You've guessed it.")
            print("De hoofdstad van {} is inderdaad {}!\n".format(land, hoofdstad))
            # De lus breken
            break
        else:
            if aantal_pogingen - i == 0:
                print("U hebt het helaas niet kunnen raden :(")
                print("De hoofdstad van {} is {}!\n".format(land, hoofdstad))
            else:
                print("Dit is helaas niet juist. U hebt nog {} poging(en) over".format(aantal_pogingen - i))
        i += 1


# 1. Welcome
print("\nWelkom bij onze Geography Quiz")

# 2. Hoofdsteden initialiseren in een dictionary
countries_cities = {"Oostenrijk": "Wenen", "Belgie": "Brussel", "Frankrijk": "Parijs", "Spanje": "Madrid",
                    "Duitsland": "Berlijn", "Portugal": "Lissabon", "Engeland": "Londen", "Zweden": "Stockholm",
                    "Denemarken": "Copenhagen", "Finland": "Helsinki", "Zwitserland": "Bern", "Turkije": "Ankara",
                    "San Marino": "San Marino", "Ierland": "Dublin", "Griekenland": "Athene", "Kosovo": "Pristina",
                    "Rusland": "Moskou"}

# 3. Main loop
while True:
    boodschap = '\nWil U het (E)asy, (M)edium of (Hard) level? '
    level = lees_letter(boodschap, ['E', 'M', 'H'])
    if level == 'E':
        # Easy - Speel het spel met 5 pogingen
        speel_quiz(countries_cities, 5)
    elif level == 'M':
        # Medium - Speel het spel met 3 pogingen
        speel_quiz(countries_cities, 3)
    else:
        # Hard - Speel het spel met 1 poging
        speel_quiz(countries_cities, 1)

    # Vragen of de gebruiker nog een spel wil spelen
    boodschap = 'Wil U nog eens spelen (J/N)? '
    nog_eens = lees_letter(boodschap, ['J', 'N'])
    if nog_eens == "N":
        # De main loop breken
        break

# 4. Afscheid
print("\nBedankt voor het spelen. Hope to see you soon...")