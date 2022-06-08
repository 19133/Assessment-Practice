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
ticket_count = 0

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


# Checks for an integer more than 0
def int_check(question):

  error = "Please enter a whole number that is more than 12 but less than 130 "
  
  valid = False
  while not valid:

    # ask user for number and check if it is valid
    try:
      response = int(input(question))

      if response <= 0:
        print (error)
      else:
        return response

    # if an integer is not entered, display an error
    except ValueError:
        print(error)


# ******* Main Routine *******

# Set up dictionaries / list needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details:

# start of loop

# initialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

while name != "xxx" and ticket_count < MAX_TICKETS:

    if ticket_count <  MAX_TICKETS -1:
        print("You have {} seats" " left".format(MAX_TICKETS - ticket_count))

        # Warns user that only one seat is left!
    else:
        print("*** There is ONE seat left!!***")

    # Get details...

    # Get name (Can't be blank)
    name = not_blank("Name: ")

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # Get age (between 12 and 130)
    age = int_check("Age: ")

    # Check if age is valid
    if age < 12:
      print("Sorry you are too young for this movie")
      continue
    elif age > 130:
      print("That is very old - it looks like a mistake")
      continue

    if age < 16:
      ticket_price = 7.5
    elif age < 65:
      ticket_price = 10.5
    else:
      ticke_price = 6.5

    ticket_count += 1
    ticket_sales += ticket_price

# End of ticket Look
# Calculate ticket profit...
ticket_profit = ticket_sales - (5* ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets... 
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available".format(ticket_count,
                                                       MAX_TICKETS - ticket_count))

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for a payment metohd (and apply surcharge if necessary)

# Calculate Total sales and profit

# Output data to text file
