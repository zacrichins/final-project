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
		new_room = self.current_room.get_exit(direction)
		if new_room is None:
			print("You cannot go that way")
		else:
			self.current_room = new_room

	def get_current_room_description(self):
		return self.current_room.description

reactorfourcontrolroom = "Reactor 4 control room: Large crescent shaped room where reactor 4 is monitored."
mcrhallway = "Hallway from reactor 4 control room"
br = "Break Room: There is a sandwhich on the table. "
dcr = "Dosimetry Control Room: You notice a large dosimeter that is powerless."
sr = "Storage room: There is a small dosimeter next to a dead body. The body is blood red and has warts and blisters all over. "
wpr = "Water pump room: There is about a foot of water on the ground and hundreds of water pumps all with levers and switches."
gr = "Generator room: Tall open room. The generator only turns on when the power plant is not producing enough power. The generator is off."
basementhallway = "Basement hallway: Your co-worker is crawling on the floor in serious pain"

room1 = Room(1, "Kitchen", "You are in a large kitchen with a long dining table in the center.", {"north": None, "south": 2, "east": None, "west": None})
room2 = Room(2, "Living Room", "You are in a spacious living room with a fireplace and a big sofa.", {"north": 1, "south": 3, "east": None, "west": None})
room3 = Room(3, "Bedroom", "You are in a cozy bedroom with a comfortable bed and a small window.", {"north": 2, "south": None, "east": None, "west": None})

game_map = GameMap([room1, room2, room3])


class Player():
	def __init__(self):
		self.inventory = []
		self.position = 0
def save(player):
	pass
def load():
	pass

player = Player()
def main(player):
	commands()
	choice = None
	while choice != "q":
		print(game_map.get_current_room_description())
		choice = input("What is your choice:\n")
		if choice == "g":
			pass
		elif choice == "u":
			pass
		elif choice == "c":
			commands()
		elif choice =="i":
			pass
		elif choice =="m":
			pass
		elif choice == "s":
			save(player)
		elif choice == "l":
			load()
		elif choice == "q":
			print("Thanks for playing!")
		else:
			print("Not valid choice")

main(player)

