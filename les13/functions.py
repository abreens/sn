####
#
# Les 13 - OOP
#
# Module die alle funkties bevat voor de oefeningen van Les 13. Aangezien er geen code staan in the Global Scope
# van deze module zullen we ook geen "if __name__ == "__main__":" statement toevoegen
#
#####


# FUNKTIE - Print algemene boodschappen voor de gebruiker. Voor de fun in een funktie gegoten ;)
def say_hello(msg):
    print(msg)


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
def lees_strg(msg_for_user):
    while True:
        invoer = input(msg_for_user)
        # Empty strings return False!
        if not invoer:
            print("Uw invoer mag niet leeg zijn. Gelieve opnieuw in te voeren...")
        else:
            # De lus breken
            break
    return invoer


# FUNKTIE - Inlezen van een geheel getal tussen <lower_limit> en <upper_limit>
def lees_geheel(lower_limit, upper_limit):
    while True:
        invoer = input("\nGeef een getal (tussen " + str(lower_limit) + " en " + str(upper_limit) + "): ")
        try:
            getal = int(invoer)
        except ValueError:
            print("Jammer genoeg was dit geen (geheel) getal. Probeer aub opnieuw...")
        else:
            if lower_limit <= getal <= upper_limit:
                # De lus breken
                break
            else:
                print("Het getal moet tussen " + str(lower_limit) + " en " + str(upper_limit) + " liggen. Probeer aub "
                                                                                                "opnieuw...")
    return getal
