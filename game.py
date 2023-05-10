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
		time.sleep(0.0001)
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
	def __init__(self, id, name, description, exits, items):
		self.id = id
		self.name = name
		self.description = description
		self.exits = exits
		self.items = items
	def get_exit(self, direction):
		return self.exits.get(direction)
	
	def use_item(self, player):
		pass
	def show_inventory(self, player):
		print(f"{player.inventory}")


class GameMap(Room):
	def __init__(self, rooms):
		self.rooms = rooms
		self.current_room = rooms[0]
		super().

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
	def grab(self, player):
		if self.items:
			pick = input("What would you like to grab?\n").lower()
			if pick in self.items:
				print(f"You picked up {pick}")
				player.inventory.append(pick)
				self.items = ""
			else:
				print(f"{pick} is not in the room")
		else:
			print("Nothing to grab")

class Player():
	def __init__(self):
		self.inventory = []
	def use(self):
		pass


room1 = Room(1, "Reactor 4 control room", "\n\nReactor 4 control room: Large crescent shaped room where reactor 4 is monitored.\nExits: south", {"north": None, "south": 2, "east": None, "west": None}, None)
room2 = Room(2, "Break Room", "\n\nBreak Room: There is a sandwhich on the table.\nExits: north, south", {"north": 1, "south": 3, "east": None, "west": None}, "Sandwhich")
room3 = Room(3, "Dosimetry Control Room", "\n\nDosimetry Control Room: You notice a large dosimeter that is powerless.\nExits: north, east", {"north": 2, "south": None, "east": 4, "west": None}, None)
room4 = Room(4, "Storage Room", "\n\nStorage Room: there is a small dosimeter next to a dead body.\nExits: west, south", {"north": None, "south": 5, "east": 3, "west": None}, "dosimeter")
room5 = Room(5, "Water Pump Room", "Water Pump Rooom: there is about a foot of water on the ground and pumps and levers all over", {"north": 4, "south": None, "east": None, "west": None}, None)

game_map = GameMap([room1, room2, room3, room4])

def save():
	with open("save.dat", "wb") as file:
		pickle.dump(Player, file)
		pickle.dump(GameMap, file)
		pickle.dump(Room, file)
		print("Game Saved")
def load():
	try:
		with open("save.dat","rb") as file:
			pickle.load(file)
	except FileNotFoundError:
		print("File not found")

player = Player()
def main():
	commands()
	choice = None
	while choice != "q":
		print(game_map.get_current_room_description())
		choice = input("What is your choice:\n")
		if choice == "g":
			game_map.grab(player)
		elif choice == "u":
			game_map.use_item(player)
		elif choice == "c":
			commands()
		elif choice =="i":
			game_map.show_inventory(player)
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

