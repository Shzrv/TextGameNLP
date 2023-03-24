# in NLTK:

import nltk

predefined_cmd = ["go left"]
cmd = "The big brown dog chased the cat in South Africa. "

# tokenize the string - means split to words and other meaning fragments like periods, commas and n't
tokens = nltk.word_tokenize(cmd)

# tag the list of tokens with parts of speech
tagged = nltk.pos_tag(tokens)

# group the words into meaningful segments (example - "South Africa" is a seen as a single phrase)
print(nltk.chunk.ne_chunk(tagged))
