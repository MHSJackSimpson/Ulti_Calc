# Generates headings (eg: ----- Heading -----)
# Generates headings (eg: ----- Heading -----)

def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
-Follow the instructions given later on in the program.
-Please answer in lower case.
-type "xxx" when you wish to exit the program.
    ''')


def get_domain():
    error = "\nPlease enter an appropriate DOMAIN (mass, distance or time)"
    while True:

        response = input("\nPlease choose a Domain: ")

        if response == "xxx":
            break

        if response in ['mass', 'm']:
            return "mass"

        if response in ['time', 't']:
            return "time"

        if response in ['distance', 'd', 'dis']:
            return "distance"

        else:
            print(error)


def get_unit(valid_list):
    error = f"\nPlease enter an appropriate UNIT!, choose from {valid_list}"
    while True:

        response = input("Please enter a unit: ").lower()

        if response == "xxx":
            break
        if response in valid_list:
            return response
        else:
            print(error)


def int_check(question, low):
    error = "Please enter a number with a value greater than 0 :)\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))
            if response == "xxx":
                break
            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

# Main routing goes here


# list of units
mass_units = ["mg", "g", "kg"]
distance_units = ['mm', 'cm', 'm', 'km']
time_units = ['sec', 'min', 'hrs', 'days']

want_instructions = input("Press <enter> to read the instructions " "or any key to continue ")

if want_instructions == "":
    instructions()


print("program continues")

domain = get_domain()

print("Domain:", domain)

if domain == "mass":
    unit_list = mass_units
elif domain == "distance":
    unit_list = distance_units
else:
    unit_list = time_units

from_unit = get_unit(unit_list)
to_unit = get_unit(unit_list)

print(f"\nYou chose to go from {from_unit} to {to_unit}\n")

distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001,
}

mass_dict = {
    "mg": 1000,
    "g": 1,
    "kg": 0.001,
}


time_dict = {
    "sec": 86400,
    "min": 1440,
    "hrs": 24,
    "days": 1,
}

amount = float(input("How much? "))
if domain == "distance":
    diction = distance_dict
if domain == "mass":
    diction = mass_dict
elif domain == "time":
    diction = time_dict

# standard value
multiply_by = diction[to_unit]
standard = amount * multiply_by

# desired value
divide_by = diction[from_unit]
answer = standard / divide_by


print(f"\nThere is {answer} {to_unit} in {amount} {from_unit} ")

keep_going = input("\nPress 'ENTER' to keep going or type 'xxx' then press enter to quit! ")
print("Thank you for using this program :)")
