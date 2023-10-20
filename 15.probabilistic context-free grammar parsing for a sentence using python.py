import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser
from nltk.grammar import Nonterminal

# Define a PCFG grammar
grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.4] | 'John' [0.3] | 'I' [0.3]
    VP -> V NP [0.7] | 'ate' [0.3]
    Det -> 'the' [0.6] | 'an' [0.4]
    N -> 'apple' [0.5] | 'pie' [0.5]
    V -> 'ate' [1.0]
""")

# Define a sentence
sentence = "I ate the apple"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Create a parser
parser = ViterbiParser(grammar)

# Parse the sentence and print the most likely parse tree
for tree in parser.parse(tokens):
    tree.pretty_print()
