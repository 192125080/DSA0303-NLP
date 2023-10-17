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

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Define a different sentence to parse
sentence = "the cat chased the dog".split()

# Generate and print parse trees
for tree in parser.parse(sentence):
    tree.pretty_print()
