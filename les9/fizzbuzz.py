#####
# Les 9 - FIZZBUZZ
#
# User enters a number between 1 and 100
# FizzBuzz program starts to count to that number (it prints them in the Terminal).
# In case the number is divisible with 3, it prints "fizz" instead of the number.
# If the number is divisible with 5, it prints "buzz".
# If it's divisible with both 3 and 5, it prints "FIZZBUZZ".
#
#####


# FUNKTIE - Inlezen van een geheel getal tussen 1 en 100
def leesgeheel():
    while True:
        invoer = input("\nGeef een geheel getal tussen 1 en 100 aub: ")
        try:
            getal = int(invoer)
        except ValueError:
            print("Jammer genoeg was dit geen (geheel) getal. Probeer aub opnieuw...")
        else:
            if 1 <= getal <= 100:
                print("Dit was een correcte invoer! Het spel zal nu beginnen...")
                # De lus breken
                break
            else:
                print("Het getal moet tussen 1 en 100 liggen. Probeer aub opnieuw...")
    return getal


# Welcome
print("Welcome to the Smartninja FIZZBUZZ game!")

# Het getal inlezen
aantal = leesgeheel()

# Start the FuzzBizz game
i = 1
while i <= aantal:
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1

# Einde
print("Einde!")
