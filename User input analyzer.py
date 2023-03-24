# in NLTK:

import nltk


# 1. Define function that accepts user input, tokenizes it, tags it, and chunks it.
def input_process(cmd):
    # tokenize the string - means split to words and other meaning fragments like periods, commas and n't
    tokens = nltk.word_tokenize(cmd)

    # tag the list of tokens with parts of speech
    tagged = nltk.pos_tag(tokens)

    # group the words into meaningful segments
    chunked = nltk.chunk.ne_chunk(tagged)
    return chunked


# 2. define a function that checks if the command given is a move-command
def check_move_direction(tokens, direction):
    # check if this is a move command and return the input string for further processing
    return "go" or "walk" or "move" in tokens and direction in tokens


# 3. define a function that checks, what direction the user wants to move. Here, use a dictionary where one the values
# are the commands, and the keys are lambda functions that make use of the function in 2.
def determine_direction(direction):
    predefined_direction = {
        "left": lambda tokens: check_move_direction(tokens, "left"),
        "right": lambda tokens: check_move_direction(tokens, "right"),
        "forward": lambda tokens: check_move_direction(tokens, "forwards"),
        "back": lambda tokens: check_move_direction(tokens, "backwards")
    }
    for cmd, check in predefined_direction.items():
        if check(direction):
            return cmd
    return None


cmd = input("What would you like to do? ")
cmd = input_process(cmd)
matched = determine_direction(cmd)
if matched:
    print(f"you decided to go {matched}")
else:
    print("not a move command")