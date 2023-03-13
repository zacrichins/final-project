#room details
reactorfourcontrolroom = ("Reactor 4 control room: Large crescent shaped room where reactor 4 is monitored.")
rfourhallway = ("Hallway from maint control room ")
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
		time.sleep(0.03)
	print()

#introduction\
print(gamename)
print_slow("You are Vasily Ignatenko, a rookie nuclear physicist. The date is April 26 1986 and you have just been promoted to work in the Chernobyl main control room.")
print_slow("Tonight you are being directed to run a mandatory energy test. Even though the preparations are not made, the Commander demands the test to be run.")
print_slow("The test failed. Disaster strikes. Reactor 4 has exploded.")
print_slow("Escape")


inventory = []



choice = ""
choice = input("Press enter to continue")
if choice == "":
	print()
	print()
	commands = ''' 
	Controls:
	g - grab
	t - interact
	c - show controls
	i - show inventory
	n - north
	e - east
	s - south
	w - west
	u - up 1 level
	d - down 1 level
	'''
	print(commands)
	print_slow(reactorfourcontrolroom)
	print_slow("The commander has demanded that you go and find a dosimeter to find the amount of roengten(radiation per hour)")
