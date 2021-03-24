# Create the menu as a dictionary so we have items and costs
menu = {"Chicken Tikka Massala": 9.60,
        "Chicken Balti": 7.80,
        "Beef Madras": 8.10,
        "Chicken Bhuna": 7.80,
        "Lamb Bhuna": 8.10,
        "Prawn Bhuna": 8.40,
        "Lamb Rogan Josh": 8.10,
        "Chicken Vindaloo": 7.80,
        "Chicken Korma": 7.80}

# Prints the menu and costs to the customer
for item in menu:
    print(f"{item}........{menu[item]}")

# Creates an empty order for the customer to add items to
# Stops adding items when the customer ENDs their order
order = []
print("Type 'END' at any time to finish the order")
ordering = True
while ordering:
    new_item = input("Next item:    ")
    if new_item == "END":
        ordering = False
        break
    order.append(new_item)

# Prints the customer's order back to them
for item in order:
    print(item)