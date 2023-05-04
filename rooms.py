MOVEMENT = {1: "Reactor 4 control room: Large crescent shaped room where reactor 4 is monitored.", 
	    	2: "Break Room: There is a sandwhich on the table.",
			3: "Dosimetry Control Room: You notice a large dosimeter that is powerless.",
			4: "Storage Room: There is a small dosimeter next to a dead body. The body is blood red and has warts and blisters all over.",
			5: "Water Pump Room: There is about a foot of water on the ground and hundreds of water pumps all with levers and switches.",
			6: "Generator Room: Tall open room. The generator only turns on when the power plant is not producing enough power. The generator is off."
			}


class Room():
	def __init__(self):
		self.room_name = {}
		self.room_description = {}
		self.room_items = []
		self.allowed_movement = []
	def grab_item(self, player):
		pick = input("What item would you like to grab?\n")
		if pick in self.room_items:
			print(f"{pick} is now in your inventory.")
			player.inventory.append(pick)
			self.room_items.remove(pick)
	def use_item(self, player):
		print(f"Your Inventory:\n{player.inventory}")
	def description(self):
		print(rooms)




room = Room()
#reactorfourcontrolroom
r = Room()
r.room_items.append("")
r.room_description = "Reactor 4 control room: Large crescent shaped room where reactor 4 is monitored."

#controlroomhallway
#break room
#Roentgen control room
r.room_items.append("Dosimeter")
#water pump room
#generator room