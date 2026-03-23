# Mark Witkowski

# Defined rooms and their connections
rooms = {
    'Hollow Sanctum': {'South': 'Hall of Dawnlight', 'Items': []},
    'Hall of Dawnlight': {'North': 'Hollow Sanctum', 'East': 'Main Entrance', 'Items': ['Anointed Sword of Dawnlight']},
    'Main Entrance': {'North': 'Mirror Hall', 'South': 'Salted Forge', 'East': 'Hall of Dawnlight', 'West': 'Courtyard',
                      'Items': []},
    'Courtyard': {'East': 'Main Entrance', 'Items': []},
    'Mirror Hall': {'South': 'Main Entrance', 'East': 'Bell Tower', 'Items': ['Silver Mirror']},
    'Bell Tower': {'West': 'Mirror Hall', 'Items': ['Iron Bell']},
    'Salted Forge': {'North': 'Main Entrance', 'East': 'Codex Vault', 'West': 'Candle Chamber',
                     'Items': ['Binding Chain of Salt and Twine']},
    'Candle Chamber': {'East': 'Salted Forge', 'Items': ['Ashen Candle']},
    'Codex Vault': {'West': 'Salted Forge', 'Items': ['Book of the Blood Sacrifice']},
    'Exit': {}  # special room to end the game
}

# Start location
current_room = 'Courtyard'


# Function to move between rooms
def move(direction):
    global current_room
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        print("You move " + direction + " to the " + current_room + ".")
    else:
        print("You cannot go that way.")


# Gameplay loop
while current_room != 'Exit':
    print("\nYou are currently in the " + current_room + ".")
    if rooms[current_room].get('Items'):
        print("You see the following item(s): " + ", ".join(rooms[current_room]['Items']))

    command = input("Enter a direction to move (North, South, East, West) or 'exit' to quit: ").capitalize()

    if command == 'Exit':
        current_room = 'Exit'
        print("Thanks for playing!")
    elif command in ['North', 'South', 'East', 'West']:
        move(command)
    else:
        print("Invalid command. Please enter a valid direction or 'exit'.")