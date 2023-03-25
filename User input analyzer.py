# in NLTK:
import nltk


# 1. Define function that accepts user input and tokenizes it.
def input_process(cmd):
    tokens = nltk.word_tokenize(cmd.lower())
    return tokens


# 2. define a function that checks if the command given is a move-command
# TO DO: add pos-tagging. extract verbs to determine, what command is being given. if "go" -> direction if "talk" -> NPC
def check_move_direction(tokens, input_direction):
    return "go" in tokens and input_direction in tokens


# 3. define a function that checks, what direction the user wants to move.
def determine_direction(inpt):
    predefined_direction = {
        "left": lambda tokens: check_move_direction(tokens, "left"),
        "right": lambda tokens: check_move_direction(tokens, "right"),
        "forward": lambda tokens: check_move_direction(tokens, "forwards"),
        "back": lambda tokens: check_move_direction(tokens, "backwards"),
    }

    for cmd, check in predefined_direction.items():
        if check(inpt):
            return cmd

    return None


cmd = input("What would you like to do? ")
cmd = input_process(cmd)
direction = determine_direction(cmd)
if direction:
    print(f"you decided to go {direction}")
else:
    print("not a move command")
