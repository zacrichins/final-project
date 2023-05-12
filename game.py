#Intro
import pickle

gamename = '''
   ____   _   _   _____   ____    _   _    ___    ____   __   __  _     
  / ___| | | | | | ____| |  _ \  | \ | |  / _ \  | __ )  \ \ / / | |    
 | |     | |_| | |  _|   | |_) | |  \| | | | | | |  _ \   \ V /  | |    
 | |___  |  _  | | |___  |  _ <  | |\  | | |_| | | |_) |   | |   | |___ 
  \____| |_| |_| |_____| |_| \_\ |_| \_|  \___/  |____/    |_|   |_____|
                                                                        
'''
import time
def print_slow(text):
	for char in text:
		print(char, end='', flush=True)
		time.sleep(0.01)
	print()
def print_slow2(text):
	for char in text:
		print(char, end='', flush=True)
		time.sleep(0.05)
	print()

print(gamename)
print_slow("You are Vasily Ignatenko, a rookie nuclear physicist. The date is April 26 1986 and you have just been promoted to work in the Chernobyl main control room.")
print_slow("Tonight you are being directed to run a mandatory energy test. Even though the preparations are not made, the Commander demands the test to be run.")
print_slow("The test failed. Disaster strikes. Reactor 4 has exploded.")
print_slow("Escape")

choice = input("Press enter to continue")
if choice == "":
	print()
	print()
def commands():
	print(''' 
Controls:
g - grab
u - use
c - show controls
i - show inventory
m - move
q - quit game
s - save game	
l - load game
	''')



#main code
class Room:
	def __init__(self, id, name, description, exits):
		self.id = id
		self.name = name
		self.description = description
		self.exits = exits

	def get_exit(self, direction):
		return self.exits.get(direction)

class GameMap:
	def __init__(self, rooms):
		self.rooms = rooms
		self.current_room = rooms[0]
		
	def move(self, direction):
		new_room_id = self.current_room.get_exit(direction)
		new_room = None
		for room in self.rooms:
			if room.id == new_room_id:
				new_room = room
				break
		if new_room is None:
			print("You cannot go that way")
		else:
			self.current_room = new_room

	def get_current_room_description(self):
		return self.current_room.description

room1 = Room(1, "Reactor 4 control room", "\n\nReactor 4 control room: Large crescent shaped room where reactor 4 is monitored. The Commander wants you to go find a dosimeter.\nExits: south", {"north": None, "south": 2, "east": None, "west": None})
room2 = Room(2, "Break Room", "\n\nBreak Room: There is a SANDWHICH on the table.\nExits: north, south", {"north": 1, "south": 3, "east": None, "west": None})

room3 = Room(3, "Dosimetry Control Room", "\n\nDosimetry Control Room: You notice a large dosimeter that is powerless and another small DOSIMETER you can grab.\nExits: north, east", {"north": 2, "south": None, "east": 4, "west": None})
room4 = Room(4, "Storage Room", "\n\nStorage Room: there is a POWER SWITCH next to a dead body.\nExits: west, south", {"north": None, "south": 5, "east": 3, "west": None})

room5 = Room(5, "Water Pump Room", "\n\nWater Pump Rooom: there is about a foot of water on the ground and pumps and levers all over.\nExits: north, west", {"north": 4, "south": None, "east": None, "west": 6})
room6 = Room(6, "Generator Room", "\n\nGenerator room: Tall open room. The generator needs to be turned on, it needs a power switch.\nExits: south, east", {"north": None, "south": 7, "east": 5, "west": None})
room7 = Room(7, "Basement Hallway", "\n\nBasement hallway: Your co-worker is crawling on the floor in serious pain, he could use something to eat.\nExits: north, west", {"north": 6, "south": None, "east": None, "west":8})
room8 = Room(8, "Exit Room", "\n\nExit Room: There is a solid metal door. You need a key and paper with code to escape\nExits: east", {"north": None, "south":None, "east": 7, "west":None})

game_map = GameMap([room1, room2, room3, room4, room5, room6, room7, room8])
 
items = ["dosimeter", "sandwhich", "power switch"]
inventory = []
def grab():
	if game_map.current_room.id == 2:
		pick = input("What item would you like to grab?\n").lower()
		if pick in items and pick == "sandwhich":
			inventory.append(pick)
			items.remove(pick)
			print_slow2(f"You grabbed {pick}")
		else:
			print("That item doesn't exist")
	elif game_map.current_room.id == 3:
		pick = input("What item would you like to grab?\n").lower()
		if pick in items and pick == "dosimeter":
			inventory.append(pick)
			items.remove(pick)
			print_slow2(f"You grabbed {pick}")
		else:
			print("That item doesn't exist")
	elif game_map.current_room.id == 4:
		pick = input("What item would you like to grab?\n").lower()
		if pick in items and pick == "power switch":
			inventory.append(pick)
			items.remove(pick)
			print_slow2(f"You grabbed {pick}")
		else:
			print("That item doesn't exist")
	else:
		print("There are no items to pick up")


def use():
	global game_map
	if game_map.current_room.id == 1:
		if "dosimeter" in inventory:
			print_slow2("You give the dosimeter to the Commmander and he says everything is fine. The radiation levels are normal but you think otherwise.")
			inventory.remove("dosimeter")
		else:
			print("You have nothing to use")
	elif game_map.current_room.id == 6:
		if "power switch" in inventory:
			print_slow2("You use the power switch on the generator and the lights turn on in the room. You now notice a piece of paper with a code on it. You grab the paper.")
			inventory.remove("power switch")
			inventory.append("paper")
		else:
			print("You have nothing to use")
	elif game_map.current_room.id == 7:
		if "sandwhich" in inventory:
			print_slow2("You gave the sandwhich to your coworker. He may have a chance of surviving. He gives you a key")
			inventory.append("key")
			inventory.remove("sandwhich")
		else:
			print("You have nothing to use")
	elif game_map.current_room.id == 8:
		if "key" and "paper" in inventory:
			print_slow2("You escaped Chernobyl...")
			win = True
			return win

		else:
			print("You don't have both the key and paper")
	
	else:
		print("You can't use any items in this room")



def save():
	with open("save.dat", "wb") as file:
		pickle.dump(game_map, file)
		pickle.dump(inventory, file)
		pickle.dump(items, file)
		print("Game Saved")
def load():
	try:
		with open("save.dat","rb") as file:
			inventory = pickle.load(file)
			game_map = pickle.load(file)
			items = pickle.load(file)
			print("Game Loaded")
	except FileNotFoundError:
		print("File not found")

#game loop
def main():
	commands()
	choice = None
	while choice != "q":
		print(game_map.get_current_room_description())
		choice = input("What is your choice:\n").lower()
		if choice == "g":
			grab()
		elif choice == "u":
			win = use()
			if win == True:
				break
		elif choice == "c":
			commands()
		elif choice =="i":
			print(inventory)
		elif choice =="m":
			direction = input("Which direction would you like to move?\n").lower()
			game_map.move(direction)
		elif choice == "s":
			save()
		elif choice == "l":
			load()
		elif choice == "q":
			print("Thanks for playing!")
		else:
			print("Not valid choice")

main()

