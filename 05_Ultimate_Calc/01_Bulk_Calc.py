# Generates headings (eg: ----- Heading -----)
while True:
    def statement_generator(statement, decoration):
        print(f"\n{decoration * 5} {statement} {decoration * 5}")


    # Displays instructions
    def instructions():
        statement_generator("Instructions", "-")

        print('''
    -Choose a unit of measurement (E.g: mm, msec, days, hrs or kg)
    -Follow the instructions given later on in the program
    -type "xxx" when you wish to exit the program.
        ''')


    # Main routine goes here

    want_instructions = input("Press <enter> to read the instructions " "or any key to continue ")

    if want_instructions == "":
        instructions()

        if want_instructions == "xxx":
            break

    print("program continues")


    def get_unit_old():
        error2 = "\nPlease enter an appropriate UNIT!"
        while True:

            response = input("\nPlease enter the unit you wish TO convert: ")

            if response == "xxx":
                break
            if response == ['mm', 'cm', 'm', 'km', 'msec', 'sec', 'min', 'hrs', 'days', 'mg', 'g', 'kg', 't']:
                return response
            else:
                print(error2)
                get_unit_old()


    def get_unit_new():
        error3 = "\nPlease enter an appropriate UNIT (You can't convert days into mm)!"
        while True:

            response = input("\nPlease enter the unit you wish to convert INTO: ")

            if response == "xxx":
                break
            if response == ['mm', 'cm', 'm', 'km', 'msec', 'sec', 'min', 'hrs', 'days', 'mg', 'g', 'kg', 't']:
                return response
            else:
                print(error3)
                get_unit_new()


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


    def bulk_calc(question):
        while True:
            old = get_unit_old
            new = get_unit_new
            int_check("NUMBER: ", 1)
            response = int(input(question))
            # Measurement calc part 1
            if response == "xxx":
                break

            if old == 'mm' and new == 'cm':
                answer = response / 10

                return answer

            if old == 'mm' and new == 'm':
                answer = response / 1000

                return answer

            if old == 'mm' and new == 'km':
                answer = response / 1000000

                return answer

            if old == 'cm' and new == 'mm':
                answer = response * 10

                return answer

            if old == 'm' and new == 'mm':
                answer = response * 1000

                return answer

            if old == 'km' and new == 'mm':
                answer = response * 1000000

                return answer
            # Measurement calc part 2

            # Weight calc part 1

            # Weight calc part 2

            # Time calc part 1

            # Time calc part 2

    while True:
        old = get_unit_old()
        new = get_unit_new()


