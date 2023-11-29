# Jeffrey Chen
# Adventure Game V2

import time

keys = {
    "vKey": 0,
    "rKey": 0,
    "bKey": 0
}


c = (".")


# Provides directions for the player
print("Welcome to Unknown's House!" + "\n" + "Complete the objectives and escape.")
print("When prompted for an action, type a direction to go [north, east, south, west]." + "\n" + "Good Luck!" + "\n")
print("You wake up in a dark room..." + "\n" + "You find a door to the north and east." + "\n")

unlocked = {
    'vaultUnlocked': 'no',
    'gunUnlocked': 'no',
    'safeUnlocked': 'no',
    'deskUnlocked': 'no',
    'westStairs': 'no'
}

quest = ['Find and obtain the map.', 'Find the laser pointer.']

found = []

game = {
    
}

# Define rooms and provide descriptions for each room
rooms = {
	# Description and navigation for the room that the player will start in
    "start": {
        "description": "\n" + "You are in a dark room. There is a door to the north and east.",
        "north": "lobby",
        "east": "bathroom"
    },
	# Description and navigation for the Lobby
    "lobby": {
        "description": "\n" + "You are in the Lobby. There is a door to the north, east, west, and south." + "\n",
        "east": "kitchen",
        "south": "start",
        "north": "armory",
        "west": "hallway"
    },
	# Description and navigation for the Kitchen
    "kitchen": {
        "description": "\n" + "You are in the Kitchen. There is a door to the west and south." + "\n",
        "west": "lobby",
        "south": "bathroom"
    },
	# Description and navigation for the Armory
    "armory": {
        "description": "\n" + "You are in the Armory. There is a door to the south and east." + "\n",
        "south": "lobby",
        "east": "locker"
    },
	# Description and navigation for the Bathroom
    "bathroom": {
        "description": "\n" + "You are in the Bathroom. There is a door to the west and north. You see a huge vault door to the south..." + "\n",
        "west": "start",
        "north": "kitchen",
        "south": "vault"
    },
	# Description and navigation for the Vault
    "vault": {
        "description": "\n" + "You are in the vault." + "\n" + "There is a door to the north." + "\n",
        "north": "bathroom"
    },
        # Description and navigatiton for the Hallway
    "hallway": {
        "description": "\n" + "You are in a dark hallway. You find a door to the north and stairs leading down to the west." + "\n",
        "north": "storage",
        "west": "stairs",
        "east": "lobby"
    },
        # Description and navigatiton for the Storage room
    "storage": {
        "description": "\n" + "You are in a dusty storage room. You find a door to the north and south." + "\n",
        "north": "office",
        "south": "hallway"
    },
        # Description and navigatiton for the Office
    "office": {
        "description": "\n" + "You are in an old office. There is a desk with a locked compartment. It seems to be asking for a coordinate (_ _ _ _, _ _ _ _). You find a door to the south." + "\n",
        "south": "storage"
    },
        # Description and navigatiton for the West Stairs
    "stairs": {
        "description": "You are on the west stairs. You find a door to the west and east",
        "west": "jailCell",
        "east": "hallway"
    },
        # Description and navigatiton for the Jail Cell
    "jailCell": {
        "description": "You see a jail cell in the room. You find a door to the east",
        "east": "stairs"
    },
        # Description and navigatiton for the Locker
    "locker": {
        "description": "You see a jail cell in the room. You find a door to the east",
        "west": "armory"
    },
    
}


# Provides options for the player
def show_room(room):
    if(current_room != {"description": "\n" + "You are in the Lobby. There is a door to the north, east, west, and south." + "\n", "east": "kitchen", "south": "start", "north": "armory", "west": "hallway"}):
        print(room["description"])

		
# Asks the user for movement input
def get_action(room):
    while True:
        action = input("What do you want to do? ").lower().strip()
        if action == "north" and "north" in room:
            return room["north"]
        elif action == "east" and "east" in room:
            if(current_room == {"description": "You see a jail cell in the room. You find a door to the east", "east": "stairs"}):
                print("You slowly walk up the stairs", sep=' ', end='', flush=True)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                print("\n")
                time.sleep(1)
                print("You feel your right foot press down on the third step and you hear a faint click.")
                time.sleep(1.5)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                time.sleep(3)
                print("\n")
                print("No arrows were shot out this time!", sep=' ', end='', flush=True)
                print("\n")
                print("You make it up the stairs safely." + "\n")
                return room["east"]
            elif current_room != {"description": "You see a jail cell in the room. You find a door to the east", "east": "stairs"}:
                return room["east"]
        elif action == "south" and "south" in room:
            if(current_room == {"description": "\n" + "You are in the Bathroom. There is a door to the west and north. You see a huge vault door to the south..." + "\n", "west": "start", "north": "kitchen", "south": "vault"} and unlocked["vaultUnlocked"] == "no"):
                enterVault = input("Would you like to see if any of your keys will unlock the vault? ")
                if enterVault.lower().strip() == "yes" and keys["vKey"] == 1:
                    print("\n" + "You insert the key with the V engraving..." + "\n" + "You hear a click..." + "\n" + "The vault door opens!" + "\n")
                    unlocked["vaultUnlocked"] = "yes"
                    keys["vKey"] = 0
                    return room["south"]
                elif enterVault.lower().strip() == "yes" and keys["vKey"] == 0:
                    print("\n" + "You try all the keys you've collected..." + "\n" + "The door won't budge!" + "\n")
            elif(current_room == {"description": "\n" + "You are in the Bathroom. There is a door to the west and north. You see a huge vault door to the south..." + "\n", "west": "start", "north": "kitchen", "south": "vault"} and unlocked["vaultUnlocked"] == "yes"):
                return room["south"]
            elif current_room != {"description": "\n" + "You are in the Bathroom. There is a door to the west and north. You see a huge vault door to the south..." + "\n", "west": "start", "north": "kitchen", "south": "vault"}:
                return room["south"]
        elif action == "west" and "west" in room:
            if(current_room == {"description": "\n" + "You are in a dark hallway. You find a door to the north and stairs leading down to the west." + "\n", "north": "storage", "west": "stairs", "east": "lobby"} and unlocked["westStairs"] == "yes"):
                print("You slowly walk down the stairs", sep=' ', end='', flush=True)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                print("\n")
                time.sleep(1)
                print("You feel your right foot press down on the third step and you hear a faint click.")
                time.sleep(1.5)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                time.sleep(3)
                print("\n")
                print("The stairs should be safe now", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                print("\n")
                time.sleep(2)
                print("You make it down the stairs safely." + "\n")
                return room["west"]
            elif(current_room == {"description": "\n" + "You are in a dark hallway. You find a door to the north and stairs leading down to the west." + "\n", "north": "storage", "west": "stairs", "east": "lobby"} and unlocked["westStairs"] == "no"):
                print("You slowly walk down the stairs", sep=' ', end='', flush=True)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                print("\n")
                time.sleep(1)
                print("You feel your right foot press down on the third step and you hear a faint click.")
                time.sleep(1)
                print(".", sep=' ', end='', flush=True)
                time.sleep(1)
                print(".", sep=' ', end='', flush=True)
                time.sleep(1)
                print(".", sep=' ', end='', flush=True)
                print("\n")
                print("You managed to react in time to dodge the four arrows that flew right by your head", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                time.sleep(2)
                print(".", sep=' ', end='', flush=True)
                print("\n")
                time.sleep(2)
                print("You make it down the rest of the stairs safely." + "\n")
                unlocked["westStairs"] = "yes"
                return room["west"]
            elif current_room != {"description": "\n" + "You are in a dark hallway. You find a door to the north and stairs leading down to the west." + "\n", "north": "storage", "west": "stairs", "east": "lobby"}:
                return room["west"]
        elif action.lower().strip() == "search":
            if(current_room == {'description': "\n" + 'You are in the Kitchen. There is a door to the west and south.' + "\n", 'west': 'lobby', 'south': 'bathroom'} and keys["rKey"] == 0 and unlocked["gunUnlocked"] == "no"):
                print("\n" + "You found a red key!" + "\n" + "I wonder what this is for?" + "\n")
                keys["rKey"] = 1
            elif(current_room == {'description': '\nYou are in the Armory. There is a door to the south and east.\n', 'south': 'lobby', 'east': 'locker'} and keys["vKey"] == 0 and unlocked["vaultUnlocked"] == "no"):
                keys["vKey"] = 1
                print("\n" + "You found a key with a V engraved on it!" + "\n" + "What could V stand for?" + "\n")
            elif(current_room == {"description": "\n" + "You are in the vault." + "\n" + "There is a door to the north." + "\n", "north": "bathroom"} and unlocked["safeUnlocked"] == "no"):
                print("You find a small dusty safe in the corner.\n")
                openSafe = input("Would you like to try and open the combination safe? ")
                if openSafe.lower().strip() == "yes":
                    keyPass = input("\nEnter the password for S153: ")
                    if mapPass == "5927":
                        found.append("map(0010, 4822)")
                        print("You found a map.")
            elif(current_room == {"description": "\n" + "You are in an old office. There is a desk with a locked compartment. It seems to be asking for a coordinate (_ _ _ _, _ _ _ _). You find a door to the south." + "\n", "south": "storage"} and unlocked["deskUnlocked"] == "no"):
                openDesk = input("Would you like to open the numerical lock to access the locked compartment? ")
                if openDesk.lower().strip() == "yes":
                    desk = input("Enter the coordinates found on the map (e.g. 19325, 19322): ")
                    if desk == "0010, 4822":
                        found.append("laser pointer")
                        print("You found a laser pointer." + "\n" + "You completed the quest!")
            elif(current_room == {"description": "You see a jail cell in the room. You find a door to the east", "east": "stairs"}):
                print("\n" + "You find a book in the cell." + "\n" + "You hear a creaking sound." + "\n")
                jailBook = input("Would you like to get the book? ")
                if jailBook.lower().strip() == "yes":
                    print("\n" + "You walk under the gate of the cell and pick up the book", sep=' ', end='', flush=True)
                    time.sleep(2)
                    print(".", sep=' ', end='', flush=True)
                    time.sleep(2)
                    print(".", sep=' ', end='', flush=True)
                    time.sleep(2)
                    print(".", sep=' ', end='', flush=True)
                    time.sleep(2)
                    print("\n")
                    print("The gate falls and traps you in the cell." + "\n")
                    print("You open the book", sep=' ', end='', flush=True)
                    time.sleep(2)
                    print(".", sep=' ', end='', flush=True)
                    time.sleep(2)
                    print(".", sep=' ', end='', flush=True)
                    time.sleep(2)
                    print(".", sep=' ', end='', flush=True)
                    print("\n")
                    time.sleep(2)
                    print("The book contains two words:")
                    time.sleep(2)
                    print("\n")
                    print("Try ", sep=' ', end='', flush=True)
                    time.sleep(2)
                    print("A", sep=' ', end='', flush=True)
                    time.sleep(0.5)
                    print("g", sep=' ', end='', flush=True)
                    time.sleep(0.5)
                    print("a", sep=' ', end='', flush=True)
                    time.sleep(0.5)
                    print("i", sep=' ', end='', flush=True)
                    time.sleep(0.5)
                    print("n", sep=' ', end='', flush=True)
                    time.sleep(0.5)
                    print("\n")
                    for x in range(1,50):
                        print("-", sep=' ', end='', flush=True)
                    print("\n")
                    print("You find food and water in the large cell.")
                    print("You hope someone will come by to help.")
                    print("Years pass as you spend your time counting each day pass in the cell.")
                    break
            else:
                print("You didn't find anything." + "\n")
        else:
            print("Invalid action. Try again.")

# Begin game
current_room = rooms["start"]

while "escape" not in game:
    next_room = get_action(current_room)
    current_room = rooms[next_room]
    if(current_room == {'description': "\n" + 'You are in the Lobby. There is a door to the north, east, west, and south.' + "\n", 'east': 'kitchen', 'south': 'start', 'north': 'armory', 'west': 'hallway'}):
        print("\n" + "You are in the Lobby. There is a door to the north, east, west, and south." + "\n")
        viewBoard = input("Would you like to view the board? ")
        if viewBoard.lower().strip() == "yes":
            print("\n")
            print("Objectives:")
            for x in quest:
                print(x)
            print("\n")
    show_room(current_room)

        
        
        
            

