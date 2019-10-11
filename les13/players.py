#####
#
# Les 13 - OOP Players
#
# Let's make our program for basketball and football players a bit more useful. Add an option that a user can
# enter data (via input()) and at the end of the program the data gets saved in a text file.
#
# Hint: you can easily convert an object into a dictionary via the in-built __dict__ method.
# Try this in your program: lebron.__dict__ (note that there are 2 underscores on each side).
#
# Use the knowledge that you gained while building the Guess the secret number game.
#
#####

# Gezamelijke funkties importeren
import functions as f


class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


def main():

    # 1. Welcome
    f.say_hello("\nWelkom bij het Spelers Management programma")

    # 2. Hoofd loop
    while True:
        boodschap = '\nWil U A) een speler toevoegen, B) de geregistreerde spelers bekijken of C) stoppen? '
        selection = f.lees_letter(boodschap, ["A", "B", "C"])
        if selection == "A":
            boodschap = "\nWil U een (B)asketbal speler of een (V)oetbal speler toevoegen? "
            keuze = f.lees_letter(boodschap, ["B", "V"])
            if keuze == "B":
                voornaam = f.lees_strg("\nWat is Uw voornaam? ")
                print("U wil een BASKETBAL speler met naam {} toevoegen".format(voornaam))
                gele_kaarten = f.lees_geheel(0, 300)
                print("{} had {} gele kaarten in zijn carriere".format(voornaam, gele_kaarten))
            else:
                print("U wil een VOETBAL speler toevoegen")
        elif selection == "B":
            f.say_hello("U koos voor B UNDER CONSTRUCTION")
        else:
            break

    # 3. Afscheid
    f.say_hello("\nBedankt voor het gebruik van onze service. Hope to see you soon...\n")

    kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2,
                               rebounds=7.1, assists=4)

    print(kev_dur.last_name)
    print(kev_dur.rebounds)
    print(kev_dur.weight_to_lbs())
    print()

    messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575,
                           yellow_cards=67, red_cards=0)

    print(messi.first_name)
    print(messi.goals)
    print(messi.weight_to_lbs())


if __name__ == "__main__":
    main()
