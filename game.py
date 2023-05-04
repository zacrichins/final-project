#room details
from rooms import Room, rooms
import pickle

reactorfourcontrolroom = "Reactor 4 control room: Large crescent shaped room where reactor 4 is monitored."
mcrhallway = "Hallway from reactor 4 control room"
br = "Break Room: There is a sandwhich on the table. "
dcr = "Dosimetry Control Room: You notice a large dosimeter that is powerless."
sr = "Storage room: There is a small dosimeter next to a dead body. The body is blood red and has warts and blisters all over. "
wpr = "Water pump room: There is about a foot of water on the ground and hundreds of water pumps all with levers and switches."
gr = "Generator room: Tall open room. The generator only turns on when the power plant is not producing enough power. The generator is off."
basementhallway = "Basement hallway: Your co-worker is crawling on the floor in serious pain"

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
		time.sleep(0.001)
	print()
#introduction
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

print_slow(reactorfourcontrolroom)
print_slow("The commander has demanded that you go and find a dosimeter to find the amount of roengten(radiation per hour)")

class Player():
	def __init__(self):
		self.inventory = []
		self.position = 0

player = Player()
def main(player):
	commands()
	choice = None
	while choice != "q":
		print(r.description())
		choice = input("What is your choice:\n")
		if choice == "g":
			player.grab_item(player)
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

