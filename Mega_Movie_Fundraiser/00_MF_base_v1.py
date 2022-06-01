# import statements

# functions go here


# Checks if ticket name is not blank
def not_blank(question):
    Valid = False

    while not Valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry - this can't be blank")


# ******* Main Routine *******

# Set up dictionaries / list needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details:

# start of loop

# initialise loop so that it runs at least once
name = ""
count = 0

# import statements

# functions go here


# Checks if ticket name is not blank
def not_blank(question):
    Valid = False

    while not Valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry - this can't be blank. Please enter your name")


def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} and {}".format(
        low_num, high_num)

    valid = False
    while not valid:

        # ask  user for number and check if it is valid
        try:
            response = int(input(question))

            # if number is greater than or equal to 12 but less than or equal to 130. Program continues
            if low_num <= response <= high_num:
                return response
            # if age doesn't fit the requirements, print error
            else:
                print(error)

            # if an integer is not entered, display an error
        except ValueError:
            print(error)


# ******* Main Routine *******

# Set up dictionaries / list needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details:

# start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    if count < 4:
        print("You have {} seats" " left".format(MAX_TICKETS - count))

        # Warns user that only one seat is left!
    else:
        print("*** There is ONE seat left!!***")

    # Get details...

    # Get name (Can't be blank)
    name = not_blank("Name: ")

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    count += 1

    # Get age (between 12 and 130)
    age = int_check("Age: ", 12, 130)

if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available".format(count,
                                                       MAX_TICKETS - count))

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for a payment metohd (and apply surcharge if necessary)

# Calculate Total sales and profit

# Output data to text file
