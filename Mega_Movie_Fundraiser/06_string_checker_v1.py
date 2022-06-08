

# String checker functions, takes in
# question and list of valid responses
def string_chekcer(question, to_check):

  valid = False
  while not valid:
    
    response = input(question).lower()

    if response in to_check:
      return response

    else:
      for item in to_check:
        # Checks if response is the first letter of 
        # An item in the list
        if response == item[0]:
          # note: retursn the entire response
          # rather than just the first letter
          return item
    

  