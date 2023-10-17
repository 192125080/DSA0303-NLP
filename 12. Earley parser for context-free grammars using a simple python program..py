import nltk

# Define a context-free grammar
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP
    Det -> 'the'
    N -> 'dog' | 'cat'
    V -> 'chased'
""")

# Create an Earley parser with the defined grammar
parser = nltk.EarleyChartParser(grammar)

# Define a sentence to parse
sentence = "the dog chased the cat".split()

# Perform parsing
for tree in parser.parse(sentence):
    tree.pretty_print()
