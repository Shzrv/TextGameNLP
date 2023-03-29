import nltk


class Game:
    def __init__(self, current_location):
        self.current_location = current_location
        self.connections = []

    def accept_input(self):
        cmd = self.cmd = input("What would you like to do? ")
        cmd = game.input_process(cmd)
        # If movement:
        direction = game.determine_direction(cmd)
        if direction:
            pass
        # Elif talk:

    # returns a list of lists - one tokenized, the other tagged
    # TO DO: add pos-tagging. extract verbs to determine, what command is given. if "go" -> direction if "talk" -> NPC
    def input_process(self, cmd):
        tokens = nltk.word_tokenize(cmd)
        tagged = nltk.pos_tag(tokens)
        cmd_type = None
        verbs = [n[0] for n in tagged if str.startswith(str(n[1]), "V")]
        if "go" in verbs:
            cmd_type = "movement"
        elif "talk" in verbs:
            cmd_type = "talk"
        print(cmd_type)
        return tokens, cmd_type

    # define a function that checks if the command given is a move-command
    @staticmethod
    def check_move_direction(tokens, input_direction):
        return "go" in tokens and input_direction in tokens

    # TO DO: Write a constructor to turn list of game.connections into a dictionary.
    def determine_direction(self, command):
        connections = self.connections
        predefined_direction = {
            "left": lambda tokens: game.check_move_direction(tokens, "left"),
            "right": lambda tokens: game.check_move_direction(tokens, "right"),
            "forward": lambda tokens: game.check_move_direction(tokens, "forwards"),
            "back": lambda tokens: game.check_move_direction(tokens, "backwards"),
        }

        for cmd, check in predefined_direction.items():
            if check(inpt):
                print(f"you decided to go {cmd}")
                return cmd

        return None

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
start_location.NPCs = [("terminal_start", "NPCs/terminal_start"), ("mystery_device", "NPCs/mystery_device")]
NPCs = start_location.NPCs
room_2 = Location("Room 2", "Locations/Room_2.txt")
terminal = NPC("NPCs/terminal_start", "neutral", None)

game = Game(start_location)

Game.pdescribe(game.current_location)

Game.pdescribe(terminal)

Game.player_move(game, room_2)

Game.pdescribe(game.current_location)

game.input_process("I want to talk to ")