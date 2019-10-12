####
#
# Les 13 - OOP
#
# Module die alle funkties bevat voor de oefeningen van Les 13. Aangezien er geen code staan in the Global Scope
# van deze module zullen we ook geen "if __name__ == "__main__":" statement toevoegen
#
#####

# Benodigde modules importeren
import json
import os


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
            print("Dat was geen correct invoer. Probeert U het aub opnieuw...")
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


# FUNKTIE - Lees een positief decimaal getal
def lees_float(msg_for_user):
    while True:
        invoer = input(msg_for_user + "(gebruik een . om het decimaal getal in te voeren!): ")
        try:
            getal = float(invoer)
        except ValueError:
            print("Dat was geen correcte invoer. Probeer aub opnieuw...")
        else:
            if getal > 0:
                # De lus breken
                break
            else:
                print("Gelieve een positief getal (verschillend van 0) in te geven aub...")
    return getal


# FUNKTIE - Een dict inlezen vanuit file_name
def lees_dict(file_name):
    # Check if file exists
    if os.path.isfile(file_name):
        with open(file_name, "r") as tabel:
            tabel_dict = json.loads(tabel.read())
    else:
        print("ERROR: File does not exist")
    return tabel_dict


# FUNKTIE  - Een speler inlezen
def lees_speler(choice):
    print("\nDe gegevens van de nieuwe speler inlezen")

    # Gemeenschappelijke velden inlezen
    f_name = lees_str("Voornaam: ")
    l_name = lees_str("Familienaam: ")
    lengte = lees_geheel("Lengte in cm ", 140, 250)
    gewicht = lees_geheel("Gewicht in kg ", 50, 150)

    # Specifieke velden inlezen
    if choice == "B":
        # BASKETBAL speler specifics
        b_points = lees_float("Aantal gescoorde punten ")
        b_rebounds = lees_float("Aantal rebounds ")
        b_assists = lees_geheel("Aantal assists ", 0, 100)

        # BASKETBALLER samenstellen
        player = BasketballPlayer(first_name=f_name, last_name=l_name, sport="Basketbal", height_cm=lengte,
                                  weight_kg=gewicht, points=b_points, rebounds=b_rebounds, assists=b_assists)

    else:
        # VOETBAL speler specifics
        doelpunten = lees_geheel("Aantal doelpunten ", 0, 100)
        yellows = lees_geheel("Aantal gele kaarten ", 0, 100)
        reds = lees_geheel("Aantal rode kaarten ", 0, 100)

        # VOETBALLER samenstellen
        player = FootballPlayer(first_name=f_name, last_name=l_name, sport="Voetbal", height_cm=lengte,
                                weight_kg=gewicht, goals=doelpunten, yellow_cards=yellows, red_cards=reds)

    return player
