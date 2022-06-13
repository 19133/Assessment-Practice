

# Function goes here
def string_check(choice, options):

  for var_list in options:

    # if the snack is in one of the lists, return the full
    if choice in var_list:

      # Get full name of snack and put it
      # in title case so it looks nice when outputted
      chosen = var_list[0].title()
      is_valid = "yes"
      break

    # if the chosen option is not valid, set is_valid to no
    else:
      is_valid = "no"

  # if the snack is not OK - ask question again 
  if is_valid == "yes":
    return chosen
  else:
    return "invalid choice"


# Valid snacks holds list of all snacks
# Each item in valid snacks is a list with
# valid options for each snacks <full name, letter code (a - e), and possible abbreviations etc>
valid_snacks = [
  ["popcorn", "p", "corn", "a"],
  ["M&M's", "m&m's", "mms", "m", "b"], # first item is M&M
  ["pita chips", "chips", "pc", "pita", "c"],
  ["water", "w", "d"]
]

# loop three times to make testing quicker
for item in range (0, 6):
  
  # ask user for desired snack and put it in lowercase
  desired_snack = input ("Snack: ").lower()

  # check if snack is valid
  snack_choice = string_check(desired_snack, valid_snacks)
  print("Snack Choice: ", snack_choice)
      
