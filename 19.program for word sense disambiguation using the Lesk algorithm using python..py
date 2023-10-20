from nltk.corpus import wordnet
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

def perform_lesk(sentence, target_word):
    # Tokenize the sentence
    tokens = word_tokenize(sentence)

    # Perform Lesk algorithm
    sense = lesk(tokens, target_word)

    if sense is not None:
        return sense.name()
    else:
        return "No matching sense found"

# Take user input for the sentence and target word
sentence = input("Enter a sentence: ")
target_word = input("Enter the target word: ")

result = perform_lesk(sentence, target_word)
print(f"Sense for the word '{target_word}': {result}")
