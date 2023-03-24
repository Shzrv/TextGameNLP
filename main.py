class Game:
    def __init__(self):
        self.position = "Room 1"

    def print_description(self):
        # add functionality to read file and pull on descriptions based on the player position
        # such as if self.position == "Room 2" : pull on a specific file.
        print("This is a placeholder")

    def player_move(self):
        command = ""
        while command != "go left":
            command = input("What would you like to do?")
        if command == "go left":
            self.position = "Room 2"


class Location:
    def __init__(self):
        self.connections = []
        self.NPCs = []
        self.items = []
        self.description = ""


class Item:
    def __init__(self):
        self.price = 0


class NPC:
    def __init__(self):
        self.attitude = ""
        self.dialogue = {}

