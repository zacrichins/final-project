import random

# define the Room class
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.items = []

    def add_paths(self, paths):
        self.paths.update(paths)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def __str__(self):
        return self.name

# define the Item class
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

# define the Player class
class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.paths:
            self.current_room = self.current_room.paths[direction]
            print(self.current_room.description)
        else:
            print("You can't go that way.")

    def use(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                print(f"You used {item}.")
                self.inventory.remove(item)
                return
        print("You don't have that item.")

    def grab(self, item_name):
        items = self.current_room.get_items()
        for item in items:
            if item.name.lower() == item_name.lower():
                self.inventory.append(item)
                self.current_room.remove_item(item)
                print(f"You grabbed {item}.")
                return
        print("That item is not in this room.")

    def show_inventory(self):
        if len(self.inventory) == 0:
            print("Your inventory is empty.")
        else:
            print("Your inventory:")
            for item in self.inventory:
                print(item)

# define the game
def play_game():
    # create the rooms
    outside = Room("Outside", "You are outside the castle.")
    foyer = Room("Foyer", "You are in the foyer of the castle.")
    library = Room("Library", "You are in the library. There are books everywhere.")
    dining_room = Room("Dining Room", "You are in the dining room. The table is set for a feast.")
    kitchen = Room("Kitchen", "You are in the kitchen. There are pots and pans everywhere.")
    dungeon = Room("Dungeon", "You are in the dungeon. It's dark and damp.")
    throne_room = Room("Throne Room", "You are in the throne room. The king sits on his throne.")

    # add paths between rooms
    outside.add_paths({"north": foyer})
    foyer.add_paths({"south": outside, "east": library, "west": dining_room, "north": kitchen})
    library.add_paths({"west": foyer})
    dining_room.add_paths({"east": foyer})
    kitchen.add_paths({"south": foyer, "down": dungeon})
    dungeon.add_paths({"up": kitchen, "east": throne_room})
    throne_room.add_paths({"west": dungeon})

    # add items to rooms
    sword = Item("Sword", "A sharp sword.")
    outside.add_item(sword)
    key = Item("Key", "A small key.")
    library.add_item(key)
    potion = Item("Potion", "A healing potion.")
    dungeon.add_item(potion)

    # create the player
    player = Player(outside)
    print(player.current_room.description)

    # game loop
    while True:
        command = input("> ").lower().split()
        if len(command) == 0:
            continue
        if command[0] == "quit":
            print("Goodbye!")
            break
        elif command[0] == "move":
            if len(command) > 1:
                player.move(command[1])
            else:
                print("Move where?")
        elif command[0] == "use":
            if len(command) > 1:
                player.use(command[1])
            else:
                print("Use what?")
        elif command[0] == "grab":
            if len(command) > 1:
                player.grab(command[1])
            else:
                print("Grab what?")
        elif command[0] == "inventory":
            player.show_inventory()
        else:
            print("Command not recognized.")
            
play_game()
