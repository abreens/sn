#####
#
# The Sum of two numbers
#
# Let's create a function that will take two numbers as parameters and add them together.
# Call this function many times in your program, each time with different parameters.
#
#####


# FUNKTIE - Tel op
def calculate_sum(num1, num2):
    return num1 + num2


# 1e aanroep
getal1 = 5
getal2 = 12
print('De som van {} en {} is {}'.format(getal1, getal2, calculate_sum(getal1, getal2)))

# 2e aanroep
print('De som van {} en {} is {}'.format(getal1, getal2, calculate_sum(-34, 14)))

# 3e aanroep
getal1 = 2.456
getal2 = 1.4728
print('De som van {} en {} is {}'.format(getal1, getal2, calculate_sum(getal1, getal2)))

# 4e aanroep
print('De som van {} en {} is {}'.format(getal1, getal2, calculate_sum(54, 120)))

# 5e aanroep
getal1 = 0
getal2 = 1112
print('De som van {} en {} is {}'.format(getal1, getal2, calculate_sum(getal1, getal2)))
