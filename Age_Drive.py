# Ask user to input age
def age_input():
    age = input("Please enter your age: ")
    if age.upper() == "EXIT":   # Stops running if the user enters 'EXIT'
        return False    # Return False if exit condition met
    elif age.isnumeric():   # Checks the input is valid
        age = int(age)
        return age          # Return age as an int
    else:       # Asks user to try again if invalid
        print("Please enter a number or 'EXIT' if you are finished")
        return age_input()      # Retry, returning itself


# Ask user to input driver's license info
def drive_input():
    driver_license = input("Do you have a driver's license?: ").upper()
    if driver_license == "EXIT":    # Stops running if the user enters 'EXIT'
        return False    # Return False if exit condition met
    elif driver_license in yes_or_no:   # Checks input if valid
        return driver_license   # Return driver licence
    else:   # Asks user to try again if invalid input
        print("Please enter Y/N or 'EXIT' if you are finished")
        return drive_input()    # Retry, returning itself


# Output a message based on age and license
def output():
    if age >= 18 and driver_license == "Y":
        print("You can vote and drive")
    elif age >= 18:
        print("You can vote")
    elif driver_license == "Y":
        print("You can drive")
    elif age >= 16:
        print("You can't drink, but are close")
    elif age < 16:
        print("You are too young, back to school")
    else:
        print("Error: age and drive do not meet any conditions")


keep_running = True
yes_or_no = ("Y", "N")
while keep_running:
    age = age_input()       # Run age_input function to return age or False
    if not age:     # If age = False, exit condition met
        keep_running = False
        break
    driver_license = drive_input()  # Run drive_input function to return 'Y', 'N' or False
    if not driver_license:  # If driver_license = False, exit condition met
        keep_running = False
        break
    if keep_running:    # If exit condition not met, run output
        output()
