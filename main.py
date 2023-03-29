import nltk


class Game:
    def __init__(self, current_location):
        self.current_location = current_location
        self.connections = []

# Accept input. Return [tokenized and tagged]
    def accept_input(self):
        cmd = input("What would you like to do? ")
        tokens = nltk.word_tokenize(cmd)
        tagged = nltk.pos_tag(tokens)
        return tokens, tagged


# Decide if this is a move or a talk command. The problem here is that these all must be one word. Needs chunking.


    def input_process(self, tokens, tagged):

        cmd_type = None
        verbs = [n[0] for n in tagged if str.startswith(str(n[1]), "V")]
        if "go" in verbs:
            cmd_type = "movement"
        elif "talk" in verbs:
            cmd_type = "talk"
        for entity in tokens:
            if entity in self.current_location.connections or entity in self.current_location.NPCs:
                target = entity
        print(cmd_type)
        return target, cmd_type

    @staticmethod
    def pdescribe(entity):
        with open(entity.description) as d:
            print("\n", d.read())

    def player_move(self, move_command):
        cmd = move_command[0]
        if game.connections in cmd:
            location = set(cmd).intersection(game.connections)
            self.current_location = location
        print(f"You find yourself in {self.current_location.name}")


class Location:
    def __init__(self, name, description_path):
        self.description = description_path
        self.name = name
        self.NPCs = []


class NPC:
    def __init__(self, description_path, attitude, dialogue):
        self.description = description_path
        self.attitude = attitude
        self.dialogue = dialogue


start_location = Location("start", "Locations/Space_Station.txt")
start_location.NPCs = [("terminal_start", "NPCs/terminal_start"),
                       ("mystery_device", "NPCs/mystery_device")]
NPCs = start_location.NPCs
room_2 = Location("Room 2", "Locations/Room_2.txt")
terminal = NPC("NPCs/terminal_start", "neutral", None)

game = Game(start_location)

Game.pdescribe(game.current_location)

Game.pdescribe(terminal)

Game.player_move(game, room_2)

Game.pdescribe(game.current_location)

game.input_process("I want to talk to ")
