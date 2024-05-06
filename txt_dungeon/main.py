import os
from PIL import Image

img = Image.open(map.png)
img.show()


# display starting menu
def prompt():
    print("\t\t\tWelcome to TEXT DUNGEON\n\n"
          "You must collect all six items before fighting the boss.\n\n"
          "Moves:\t'go {direction}' (travel north, south, east, or west)\n"
          "\t'get {item}' (add nearby item to inventory)\n\n")

    input("Press any key to continue...")


# clears screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Map
rooms = {
    'Liminal Space': {'North': 'Mirror Maze', 'South': 'Bat Cavern', 'East': 'Bazaar'},
    'Mirror Maze': {'South': 'Liminal Space', 'Item': 'Crystal'},
    'Bat Cavern': {'North': 'Liminal Space', 'East': 'Volcano', 'Item': 'Staff'},
    'Bazaar': {'West': 'Liminal Space', 'North': 'Meat Locker', 'East': 'Dojo', 'Item': 'Altoids'},
    'Meat Locker': {'South': 'Bazaar', 'East': 'Quicksand Pit', 'Item': 'Fig'},
    'Quicksand Pit': {'West': 'Meat Locker', 'Item': 'Robe'},
    'Volcano': {'West': 'Bat Cavern', 'Item': 'Elderberry'},
    'Dojo': {'West': 'Bazaar', 'Boss': 'Shadow Man'}
    }

# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# inventory
inventory = []

current_room = "Liminal Space"

# result of the last move
msg = ""

clear()
prompt()

# gameplay loop
while True:

    clear()

    # display player info
    print(f"You are in the {current_room}\n"
          f"Inventory: {inventory}\n"
          f"{'-' * 27}")

    # display message
    print(msg)

    # item indicator
    if "Item" in rooms[current_room].keys():

        nearby_item = rooms[current_room]["Item"]

        if nearby_item not in inventory:
            # plural item
            if nearby_item[-1] == 's':
                print(f"You see {nearby_item}")

            # singular item starts with a vowel
            elif nearby_item[0] in vowels:
                print(f"You see an {nearby_item}")

            # Singular starts with consonant
            else:
                print(f"You see a {nearby_item}")

    # boss encounter
    if "Boss" in rooms[current_room].keys():
        # lose
        if len(inventory) < 6:
            print(f"You lost a fight with {rooms[current_room]['Boss']}.")
            break
        # win
        else:
            print(f"You beat {rooms[current_room]['Boss']}!")
            break

    # accept player's move as input
    user_input = input("Enter your move:\n")

    # split move into words
    next_move = user_input.split(' ')

    # first word is action
    action = next_move[0].title()

    if len(next_move) > 1:

        item = next_move[1:]
        direction = next_move[1].title()

        item = ' '.join(item).title()

    # moving between rooms
    if action == "Go":
        try:
            current_room = rooms[current_room][direction]
            msg = f"You travel {direction}."
        except:
            msg = "You can't go that way"

    # picking up items
    elif action == "Get":

        try:
            if item == rooms[current_room]["Item"]:

                if item not in inventory:
                    inventory.append(rooms[current_room]["Item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}."

            else:
                msg = f"Can't find {item}."
        except:
            msg = f"Can't find {item}."

    # exit game
    elif action == "Exit":
        break

    # any other command's invalid
    else:
        msg = "Invalid Command"
