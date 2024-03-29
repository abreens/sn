####
#
# Les 13 - OOP
#
# Module die alle funkties bevat voor de oefeningen van Les 13. Aangezien er geen code staat in the Global Scope
# van deze module werd er ook geen "if __name__ == "__main__":" statement toegevoegd
#
#####


# Benodigde modules importeren
import json
import os
import random
import datetime


# Model definitions voor SPELERS
class Player:
    def __init__(self, first_name, last_name, sport, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.sport = sport
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, sport, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, sport=sport,
                         height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, sport, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, sport=sport,
                         height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


# Model definition for Guess the Secret Number RESULTS
class Result:
    def __init__(self, score, player_name, dts):
        self.score = score
        self.player_name = player_name
        self.dts = dts  # dts = Date Time Stamp


# FUNKTIE - Print een algemene boodschap voor de gebruiker.
def say_hello(msg):
    print()
    print("-" * len(msg))
    print(msg)
    print("-" * len(msg))


# FUNKTIE - Letter inlezen van lijst [mogelijkheden]. Zowel kleine als hoofdletter zijn toegestaan.
def lees_letter(msg_for_user, mogelijkheden):
    while True:
        invoer = input(msg_for_user)
        invoer = invoer.upper()
        if invoer in mogelijkheden:
            # De lus breken
            break
        else:
            print("Dat was geen correcte invoer. Probeert U het aub opnieuw...")
    return invoer


# FUNKTIE - Inlezen en kontroleren van een string
def lees_str(msg_for_user):
    while True:
        invoer = input(msg_for_user)
        # Empty strings return False!
        if not invoer:
            print("Uw invoer mag niet leeg zijn. Gelieve opnieuw in te voeren...\n")
        else:
            # De lus breken
            break
    return invoer


# FUNKTIE - Inlezen van een geheel getal tussen <lower_limit> en <upper_limit>
def lees_geheel(msg_for_user, lower_limit, upper_limit):
    while True:
        invoer = input(msg_for_user + "(gelegen tussen " + str(lower_limit) + " en " + str(upper_limit) + "): ")
        try:
            getal = int(invoer)
        except ValueError:
            print("Jammer genoeg was dit geen (geheel) getal. Probeer aub opnieuw...\n")
        else:
            if lower_limit <= getal <= upper_limit:
                # De lus breken
                break
            else:
                print("Het getal moet tussen " + str(lower_limit) + " en " + str(upper_limit) + " liggen. Probeer aub "
                                                                                                "opnieuw...\n")
    return getal


# FUNKTIE - Lees een positief reëel getal
def lees_float(msg_for_user):
    while True:
        invoer = input(msg_for_user + "(gebruik een . om een decimaal getal in te voeren!): ")
        try:
            getal = float(invoer)
        except ValueError:
            print("Dat was geen correcte invoer. Probeer aub opnieuw...\n")
        else:
            if getal > 0:
                # De lus breken
                break
            else:
                print("Gelieve een positief getal (verschillend van 0) in te geven aub...\n")
    return getal


# FUNKTIE - Een lijst van dictionaries inlezen vanuit file_name
def lees_db(file_name):
    # Check if file exists
    if os.path.isfile(file_name):
        # Bestand bestaat
        with open(file_name, "r") as db_tabel:
            # Records inlezen
            list_dicts = json.loads(db_tabel.read())
        # Empty lists return False
        if not list_dicts:
            print("\nEr is nog geen data opgeladen!")
        return list_dicts
    else:
        print("\nERROR: File '" + file_name + "' does not exist!")


# FUNKTIE - Lijst van bestaande data in spelers.txt of results.txt ophalen en afdrukken
def druk_records(file_name):
    data_lijst = lees_db(file_name)
    # Data wordt afgedrukt als de lijst niet leeg is en als de lijst niet de waarde None heeft
    if data_lijst and data_lijst is not None:
        if file_name == "spelers.txt":
            # Spelers uit spelers.txt afdrukken
            print("\nDe volgende spelers zijn geregistreerd:")
            for player_dict in data_lijst:
                print(player_dict)
        elif file_name == "results.txt":
            # Top Scores uit results.txt afdrukken
            print("\nDe volgende scores zijn geregistreerd:")
            # De scores eerst sorteren
            new_scores = sorted(data_lijst, key=lambda k: k['score'])
            for score_dict in new_scores:
                print("Op {} had speler {} {} pogingen nodig om het geheime nummer te raden"
                      .format(score_dict.get("dts"), score_dict.get("player_name"), score_dict.get("score")))


# FUNKTIE - Schrijf dictionary my_dict weg in de lijst van dictionaries in file_name
def schrijf_db(file_name, my_dict):
    # Check if file exists
    if os.path.isfile(file_name):
        # Bestand bestaat
        print("Data wordt opgeslagen...")
        # Huidige records ophalen
        records = lees_db(file_name)
        # Nieuwe dictionary toevoegen aan bestaande records
        records.append(my_dict)
        # Records wegschrijven
        with open(file_name, "w") as record_list:
            record_list.write(json.dumps(records))
    else:
        print("\nERROR: File '" + file_name + "' does not exist!")


# FUNKTIE  - Een nieuwe speler invoeren
def create_speler(choice):

    print("\nDe gegevens van de nieuwe speler inlezen")

    # Gemeenschappelijke velden inlezen
    f_name = lees_str("Voornaam: ")
    l_name = lees_str("Familienaam: ")
    lengte = lees_geheel("Lengte in cm ", 140, 250)
    gewicht = lees_geheel("Gewicht in kg ", 50, 150)

    # Specifieke velden inlezen
    if choice == "B":
        # Basketbal speler specifieke velden inlezen
        b_points = lees_float("Aantal gescoorde punten ")
        b_rebounds = lees_float("Aantal rebounds ")
        b_assists = lees_geheel("Aantal assists ", 0, 100)

        # Basketbal speler samenstellen
        player = BasketballPlayer(first_name=f_name, last_name=l_name, sport="Basketbal", height_cm=lengte,
                                  weight_kg=gewicht, points=b_points, rebounds=b_rebounds, assists=b_assists)
        return player

    elif choice == "V":
        # Voetbal speler specifieke velden inlezen
        doelpunten = lees_geheel("Aantal doelpunten ", 0, 100)
        yellows = lees_geheel("Aantal gele kaarten ", 0, 100)
        reds = lees_geheel("Aantal rode kaarten ", 0, 100)

        # Voetbal speler samenstellen
        player = FootballPlayer(first_name=f_name, last_name=l_name, sport="Voetbal", height_cm=lengte,
                                weight_kg=gewicht, goals=doelpunten, yellow_cards=yellows, red_cards=reds)
        # Tweede return statement om een warning van PyCharm te vermijden
        # Local variable 'player' might be referenced before assignment
        return player


# FUNKTIE - Speel het Guess the Secret Number spel
def play_game(name, lvl):
    # Initialisaties
    attempts = 0
    secret = random.randint(1, 30)
    dts = str(datetime.datetime.now())  # dts = Date Time Stamp
    wrong_guesses = []

    # Boodschap voor de gebruiker
    print("\nHET SPEL START NU!")

    # Main game loop
    while True:
        guess = lees_geheel("\nDoe een gok ", 1, 30)
        attempts += 1

        # Het antwoord analyseren
        if guess == secret:
            # Het getal werd geraden
            print("\nYou've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            print("Dit waren Uw verkeerde keuzes: ", wrong_guesses)
            print()

            # Het resultaat als een object samenstellen (niet alle beschikbare velden worden opgenomen!)
            resultaat = Result(score=attempts, player_name=name, dts=dts)

            # Het nieuwe resultaat als dictionary toevoegen aan results.txt
            schrijf_db("results.txt", resultaat.__dict__)

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
