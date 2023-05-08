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

room1 = Room(1, "Kitchen", "You are in a large kitchen with a long dining table in the center.", {"north": None, "south": 2, "east": None, "west": None})
room2 = Room(2, "Living Room", "You are in a spacious living room with a fireplace and a big sofa.", {"north": 1, "south": 3, "east": None, "west": None})
room3 = Room(3, "Bedroom", "You are in a cozy bedroom with a comfortable bed and a small window.", {"north": 2, "south": None, "east": None, "west": None})

game_map = GameMap([room1, room2, room3])