import nltk

# Define the CFG
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
""")

# Create a parser
parser = nltk.ChartParser(grammar)

# Generate sentences using the grammar
for tree in parser.parse(['the', 'dog', 'chased', 'a', 'cat']):
    tree.pretty_print()
