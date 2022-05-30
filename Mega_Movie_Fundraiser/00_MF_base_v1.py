# import statements


# functions go here

# Checks if ticket name is not blank
def not_blank(question, error_message):
  valid = False

  while not valid:   
    response = input(question)

    # if not blank, program continues
    if response != "":
      return response
      
    # If blank, show error (& repeat loop) 
    else:
      print(error_message)

# ******* Main Routine *******

# Set up dictionaries / list needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details:

  # Get name (Can't be blank)
  name = not_blank ("Name: ")
      
  # Get age (between 12 and 130)
  
  # Calculate ticket price

  # Loop to ask for snacks

  # Calculate snack price


  # Ask for a payment metohd (and apply surcharge if necessary)


# Calculate Total sales and profit

# Output data to text file

