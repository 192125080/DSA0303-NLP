from nltk.corpus import wordnet

def get_synsets(word):
    synsets = wordnet.synsets(word)
    return synsets

def explore_synsets(synsets):
    for synset in synsets:
        print(f"Synset: {synset.name()}")
        print(f"POS: {synset.pos()}")
        print(f"Definition: {synset.definition()}")
        print(f"Examples: {synset.examples()}")
        print()

# Take user input for a word
user_word = input("Enter a word to explore: ")

# Get synsets for the user input
synsets = get_synsets(user_word)

# Explore the synsets
explore_synsets(synsets)
