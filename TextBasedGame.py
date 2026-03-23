# Mark Witkowski

# Defined rooms and their connections
rooms = {
    # Villain's room
    'Hollow Sanctum':
        {'South': 'Hall of Dawnlight',
         'Items': []
         },
    'Hall of Dawnlight':
        {'North': 'Hollow Sanctum', 'East': 'Main Entrance',
         'Items': ['Anointed Sword of Dawnlight']
         },
    'Main Entrance':
        {'North': 'Mirror Hall', 'South': 'Salted Forge', 'East': 'Hall of Dawnlight', 'West': 'Courtyard',
         'Items': []
         },
    'Courtyard':
        {'East': 'Main Entrance', 'Items': []
         },
    'Mirror Hall': {'South': 'Main Entrance', 'East': 'Bell Tower',
                    'Items': ['Silver Mirror']
                    },
    'Bell Tower':
        {'West': 'Mirror Hall',
         'Items': ['Iron Bell']
         },
    'Salted Forge':
        {'North': 'Main Entrance', 'East': 'Codex Vault', 'West': 'Candle Chamber',
         'Items': ['Binding Chain of Salt and Twine']
         },
    'Candle Chamber':
        {'East': 'Salted Forge',
         'Items': ['Ashen Candle']
         },
    'Codex Vault':
        {'West': 'Salted Forge',
         'Items': ['Book of the Blood Sacrifice']
         },
}

# Provides detailed descriptions as you enter each room in the game
room_descriptions = {
    'Hollow Sanctum': (
        "The air is still within the Hollow Sanctum, as if the world itself dares not breathe. "
        "Black stone walls rise like tombs around you, and a faint whisper echoes... "
        "a memory of the Hollow King’s reign that refuses to die."
        "The Hollow King stands tall and motionless, his form draped in tattered robes that move as though alive. "
        "Beneath the hood, a faint glimmer of bone catches the light — but no eyes, no flesh, only a hollow cavity "
        "where a soul should be. His crown, forged from blackened iron, hums with whispers of the damned. "
        "When he turns toward you, the air itself recoils, and every instinct screams to flee."
    ),

    'Hall of Dawnlight': (
        "Golden light struggles to pierce through cracked stained glass, scattering weak rays across the floor. "
        "Shadows bend unnaturally here, as though recoiling from something sacred that once lived in this place."
    ),

    'Main Entrance': (
        "You stand before vast iron doors, their hinges screaming in protest whenever the wind moves them. "
        "The ground is slick with frost and dusted with old footprints that end abruptly, as if the owners were "
        "consumed by the dark."
    ),

    'Courtyard': (
        "A cold wind sweeps through the ruined castle’s Courtyard, carrying with it a silence that feels alive. "
        "Something unseen watches, and the weight of its presence chills you deeper than the winter air."
    ),

    'Mirror Hall': (
        "Shattered mirrors line the walls, reflecting fragments of your face, and others that aren’t yours. "
        "Every reflection moves a heartbeat too late, as if trapped between worlds."
    ),

    'Bell Tower': (
        "The air grows heavier as you ascend. A massive, rusted bell looms above, silent and unmoving. "
        "Whispers echo faintly in the rafters, as though voices are trapped inside the metal."
    ),

    'Salted Forge': (
        "You enter a vast chamber lit by dull embers and coated in ash. "
        "Molten metal drips in rhythmic intervals, hissing as it strikes salt-crusted stone. "
        "The smell of iron and brimstone thickens the air."
    ),

    'Candle Chamber': (
        "Dozens of melted candles cling to warped tables and the floor, their wax forming grotesque shapes. "
        "Only one flame remains, small, trembling, and defiant against the surrounding dark."
    ),

    'Codex Vault': (
        "Tall shelves tower above you, filled with books too ancient to touch. "
        "A faint red glow seeps from a pedestal at the center, where a single tome hums with a heartbeat of its own."
    ),
}

inventory = []

required_items = [
    "Anointed Sword of Dawnlight",
    "Silver Mirror",
    "Iron Bell",
    "Binding Chain of Salt and Twine",
    "Ashen Candle",
    "Book of the Blood Sacrifice"
]

# Function for instructions on how to play the game
def instructions():
    print('Welcome to Hollow Sanctum!')
    print('Collect the six items necessary to send the Hollow King back to his grave')
    print('Move commands: North, South, East, and West')
    print('Add an item to your inventory command: get "item name"')
    input('\nPress enter to begin your journey')

# Function to move between rooms
def move(direction):
    global current_room
    direction = direction.capitalize()  # Normalizes the direction just in case
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        print("\nYou move " + direction + " to the " + current_room + ".")
        print(room_descriptions[current_room])
        if current_room == 'Hollow Sanctum':
            encounter_hollow_king()
    else:
        print("You cannot go that way.")

# Function to show current room and inventory
def show_status():
    print("\nYou are currently in the " + current_room + ".")
    print("Inventory:", inventory)
    if rooms[current_room].get('Items'):
        print("You see:", ", ".join(rooms[current_room]['Items']))
    print("---------------------------")

# Function that allows the player to pick up any items in the current room.
def get_item(command):
    # Splits the player's input to extract the item name (everything after 'get')
    parts = command.split(maxsplit=1)
    if len(parts) < 2:
        print("You must specify which item to get.")
        return

    # Normalizes case for comparison
    item_requested = parts[1].strip().lower()

    # Checks if there are any items in the room
    if not rooms[current_room]['Items']:
        print("There are no items to get here.")
        return

    # Tries to find a matching item (case-insensitive)
    for item in rooms[current_room]['Items']:
        if item.lower() == item_requested:
            inventory.append(item)
            rooms[current_room]['Items'].remove(item)
            print("You picked up:", item)
            return

    # If no match was found
    print("That item is not here.")

# Function for boss encounter
def encounter_hollow_king():
    print("\nThe Hollow King rises from the shadows, his crown pulsing with a sickly red glow.")
    print("His voice scrapes like stone on bone as he speaks:")
    print("'You have come far... but do you bring the offerings that bind the hollow within?'")
    input("\nPress Enter to face your fate...")

    # Checks if the player has all the required items
    if all(item in inventory for item in required_items):
        print("\nYou stand your ground and present the sacred relics.")
        print("The Anointed Sword blazes with light, the Silver Mirror catches his reflection, and the Iron Bell tolls a death note.")
        print("The Binding Chain of Salt and Twine wraps around his form, the Ashen Candle burns black, and the Book of Blood shudders open.")
        print("The Hollow King screams as light pierces the darkness, his form collapsing into dust and silence.")
        print("\nThe curse is broken. You have defeated the Hollow King.")
        print("\nCongratulations! You survived the Hollow Sanctum.")
    else:
        missing = [item for item in required_items if item not in inventory]
        print("\nYour hands tremble, the relics are incomplete.")
        print("The Hollow King tilts his head, hollow eyes burning with cold hunger.")
        print("He reaches for you...")
        print("\nYour vision fades as his shadow tears through your body, freezing your blood where you stand.")
        print("You fall, and the last thing you see is his crown descending...claiming your soul.")
        print("\nYou were slain by the Hollow King.")
    # Ends the game after the encounter
    quit()

instructions()

# Start location
current_room = 'Courtyard'

# Gameplay loop
def main():
    global current_room
    print(room_descriptions[current_room])

    while True:
        show_status()
        command = input("Enter a direction, 'get <item>', or 'exit': ").strip().lower()

        if command == 'exit':
            print("You step back into the cold fog, the whispers fading behind you...")
            break
        elif command in ['north', 'south', 'east', 'west']:
            move(command)
        elif command.startswith('get'):
            get_item(command)
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()