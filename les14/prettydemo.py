# Volgende entry moet toegevoegd worden aan omgevingsvariabele PATH!
# C:\Users\axelb\AppData\Local\Programs\Python\Python37-32\Scripts

from prettytable import PrettyTable

table = PrettyTable(["animal", "ferocity"])

table.add_row(["wolverine", 100])
table.add_row(["grizzly", 87])
table.add_row(["cat", -1])
table.add_row(["dolphin", 63])

print(table)


