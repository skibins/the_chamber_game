import random

# Dictionary containing the types of chests and their corresponding gold amounts
chests = {'Green': 1000, 'Orange': 4000, 'Purple': 9000, 'Diamond': 16000}

# List containing possible prizes from checking a room
prizes = ['none', 'chest']

# List to store the gold amounts gained from chests
gained_gold_amounts = []


# Function to check the contents of a room
def check_room():
    # Randomly choose a prize based on probabilities
    prize_found = random.choices(prizes, [0.31, 0.69])[0]

    # If a chest is found, get its contents
    if prize_found == 'chest':
        return get_chest()
    else:
        return 'Oops! You found nothing.'


# Function to get the contents of a chest
def get_chest():
    # Randomly choose a chest color based on probabilities
    chest_color = random.choices(list(chests.keys()), [75, 20, 4, 1])[0]
    chest_gold = chests[chest_color]  # Get the gold amount from the chosen chest color
    gained_gold_amounts.append(chest_gold)  # Add the gold amount to the list of gained amounts

    # Create a message indicating the chest found and the gold gained
    message_chest_found = f'You found the {chest_color} chest! You gained {chest_gold} gold!'

    return message_chest_found
