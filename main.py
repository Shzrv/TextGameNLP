class Game:
    def __init__(self, current_location):
        self.current_location = current_location

    @staticmethod
    def pdescribe(location):
        with open(location.description) as d:
            print(d.read())

    def player_move(self, new_location):
        self.current_location = new_location
        print(f"You find yourself in {self.current_location.name}")


class Location:
    def __init__(self, name, description_path):
        self.description = description_path
        self.name = name
        self.NPCs = []
        self.items = []


class Item:
    def __init__(self):
        self.price = 0


class NPC:
    def __init__(self):
        self.attitude = ""
        self.dialogue = {}


start_location = Location("start", "Locations/Space_Station.txt")
room_2 = Location("Room 2", "Locations/Room_2.txt")

new_game = Game(start_location)

Game.pdescribe(new_game.current_location)

Game.player_move(new_game, room_2)

Game.pdescribe(new_game.current_location)