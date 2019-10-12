####
#
# Les 13 - OOP
#
# Module die alle funkties bevat voor de oefeningen van Les 13. Aangezien er geen code staan in the Global Scope
# van deze module zullen we ook geen "if __name__ == "__main__":" statement toevoegen
#
#####

# Imports
import json
import os


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
                                                                                                "opnieuw...")
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
        points = lees_geheel("Aantal gescoorde punten ", 0, 100)
        rebounds = lees_geheel("Aantal rebounds ", 0, 100)
        assists = lees_geheel("Aantal assists ", 0, 100)
    else:
        # VOETBAL speler specifics
        doelpunten = lees_geheel("Aantal doelpunten ", 0, 100)
        yellows = lees_geheel("Aantal gele kaarten ", 0, 100)
        reds = lees_geheel("Aantal rode kaarten ", 0, 100)