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



#reactorfourcontrolroom
r = Room()
r.room_items.append("")
r.room_description["Reactor 4 Control Room"] = "Large crescent shaped room where reactor 4 is monitored."
r.allowed_movement.append("east")

#controlroomhallway
#break room
#Roentgen control room
r.room_items.append("Dosimeter")
#water pump room
#generator room