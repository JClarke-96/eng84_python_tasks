# Print 'Hello' 10 times
num = 1
while num <= 10:
    print("Hello")
    num += 1


# Add names to an empty list
names = []
print("Type 'END' at any time to finish adding names")
adding = True
while adding:
    new_name = input("Next name:    ")
    if new_name == "END":
        adding = False
        break
    names.append(new_name)

# Loop through each name in the list, outputting the name in lower case
for name in names:
    list_names_lower = name.lower()
    odd_even = (len(list_names_lower)) % 2
    if odd_even == 0:
        print(f"{list_names_lower} has an even amount of letters")
    elif odd_even == 1:
        print(f"{list_names_lower} has an odd amount of letters")
    else:
        print("Error: name length not odd or even")