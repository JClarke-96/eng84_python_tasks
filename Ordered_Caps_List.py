# Creates an empty list to add to
list = []
print("Type 'EXIT' at any time to stop adding items")

# Allows user to add new items until they type 'EXIT'
adding = True
while adding:
    new_item = input("Next item:    ").upper()
    if new_item == "EXIT":
        adding = False
        break
    list.append(new_item)

# Prints the items in the list back, ordered and in caps
for item in list:
    print(f"# {(list.index(item))+1} - {item}")