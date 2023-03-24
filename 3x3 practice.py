# Create a simple text-based game where a player can move between different locations on a 3x3 grid. The player starts
# at the center of the grid. The player can input commands to move left, right, forward, or back.
# If the player tries to move outside of the grid, display a message saying they cannot move further in that direction.

import nltk
# input_process function to tokenize user input.
def input_process(command):
    command = nltk.word_tokenize(command)
    return command

# check_move_direction function to verify if the given command is a move command.
def check_move(mvmnt, direction):
    return "go" in mvmnt and direction in mvmnt


# determine_direction function to determine which direction the user wants to move.
def determine_direction(user_input):
    directions= {
        "left": lambda tokens: check_move(tokens, "left"),
        "right": lambda tokens: check_move(tokens, "right"),
        "up": lambda tokens: check_move(tokens, "up"),
        "down": lambda tokens: check_move(tokens, "down"),
    }

    for cmd, direct in directions.items():
        if direct(user_input):
            return cmd
    return None


# Create a Player class that represents the player's position on the grid and has methods to update the position
# based on user commands.
class Player:
    def __init__(self):
        self.x = 1
        self.y = 1

    def move(self, mov):
        if mov == "left":
            if self.x > 0:
                self.x = self.x - 1
            else:
                print("you are at the left edge!")
        elif mov == "right":
            if self.x < 2:
                self.x = self.x +1
            else:
                print("you are at the right edge!")
        elif mov == "down":
            if self.y > 0:
                self.y = self.y - 1
            else:
                print("you are at the bottom edge!")
        elif mov == "up":
            if self.y < 2:
                self.y = self.y + 1
            else:
                print("you are at the top edge!")
        print(f"Current position: {self.x}, {self.y}")


# game loop where the player can input commands until they decide to quit.

def main ():
    player = Player()
    while True:
        user_command = input("What do? ")

        if user_command == "quit":
            print("Goodbye")
            break

        tokens = input_process(user_command)
        direction = determine_direction(tokens)

        if direction:
            player.move(direction)
        else:
            print("invalid command")

main()





