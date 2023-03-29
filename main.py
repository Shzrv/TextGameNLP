import nltk


class Game:
    def __init__(self, current_location):
        self.current_location = current_location
        self.connections = []

    # Accept input. Return [[tokenized] and [TUPLEs tagged]]
    # TODO Consider adding a "Quit" break
    @staticmethod
    def accept_input():
        cmd = input("What would you like to do? ")
        tokens = nltk.word_tokenize(cmd)
        tagged = nltk.pos_tag(tokens)
        print(tokens, tagged)
        return tokens, tagged

    # Decide if this is a move or a talk command. The problem here is that these all must be one word. Needs chunking.
    # ! There is a problem here. Target never gets processed. SPAGHETTI

    @staticmethod
    def input_process(tokens):
        cmd_type = None
        verbs = [n[0] for n in tokens[1] if str.startswith(str(n[1]), "V")]
        if "go" in verbs:
            cmd_type = "movement"
        elif "talk" in verbs:
            cmd_type = "talk"
        return cmd_type

    @staticmethod
    def pdescribe(entity):
        with open(entity.description) as d:
            print("\n", d.read())

    def player_talk(self, talk_command):
        target = "null"
        for entity in talk_command[0]:
            if entity in self.current_location.connections or entity in self.current_location.NPCs:
                target = entity
            else:
                print("That does not exist!")
                self.accept_input()
        print(target)
        return target

# the problem here: location is made equal to a set. the set is then passed to self.current_location, which needs to
    # be a WHAT EXACTLY??
    def player_move(self, move_command):
        cmd = move_command[0]
        if self.connections in cmd:
            location = set(cmd).intersection(self.connections)
            self.current_location = location
        print(f"You find yourself in {self.current_location.name}")


class Location:
    def __init__(self, name, description_path):
        self.description = description_path
        self.name = name
        self.NPCs = {}
        self.connections = {}


class NPC:
    def __init__(self, description_path, attitude, dialogue):
        self.description = description_path
        self.attitude = attitude
        self.dialogue = dialogue


start_location = Location("start", "Locations/Space_Station.txt")
start_location.connections = {"Room2": "Locations/Room_2.txt"}
start_location.NPCs = {"terminal_start": "NPCs/terminal_start",
                       "mystery_device": "NPCs/mystery_device"}
NPCs = start_location.NPCs
terminal = NPC("NPCs/terminal_start", "neutral", None)


def main():
    game = Game(start_location)
    while True:
        game.pdescribe(game.current_location)
        inpt = game.accept_input()
        game.input_process(inpt)


main()
