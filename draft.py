import re

while True:
    type_of_changes = int(input("Type: (1) Income (2) Expenses (3) Both: "))
    if re.search(r"^(1|2|3)$", type_of_changes):
        break