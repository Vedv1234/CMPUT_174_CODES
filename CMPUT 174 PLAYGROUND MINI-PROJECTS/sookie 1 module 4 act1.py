# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: I created this program to simulate Sookie's fishing trip where she needs 
# to catch a specific number of trouts. It helped me understand while loops and conditional statements 
# in a real-world scenario.

# First I'm setting up my fishing limit constants
trouts_required = 5        # I need this many trouts for my recipe
daily_catch_limit = 7      # I can't catch more than this many fish total
catch_n_release_limit = 3  # I can only release this many non-trout fish

# Here I'm initializing my counting variables to keep track of my fishing
number_of_catches = 0  # Total fish I've caught
number_of_releases = 0 # How many fish I've released
trouts = 0            # Number of trouts I've caught

# I'll keep fishing as long as I haven't hit my daily limit AND haven't got enough trouts
while number_of_catches < daily_catch_limit and trouts < trouts_required:
    # Asking if I caught a trout
    reply = input('Trout?y/n >')
    
    if reply == 'y':  # If I caught a trout
        trouts = trouts + 1           # Add to my trout count
        number_of_catches = number_of_catches + 1  # Add to total catches
    else:  # If I caught something else
        if number_of_releases < catch_n_release_limit:  # If I can still release fish
            print('Releasing the fish !')
            number_of_releases = number_of_releases + 1 
        else:  # If I've hit my release limit
            number_of_catches = number_of_catches + 1  # Have to keep the fish
   
    # Printing my current fishing status
    print(f'{trouts} trouts caught so far')
    print(f'{number_of_catches} caught so far')
    print(f'{number_of_releases} released so far')

# Deciding what to cook based on how many trouts I caught
if trouts == trouts_required:
    print('Trout Cakes')     # Got enough trouts for my recipe!
else:
    print('Seafood Medley')  # Not enough trouts, making something else