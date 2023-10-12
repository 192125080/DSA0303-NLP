import nltk

# Define a PCNF
pcnf_grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.7] | N [0.3]
    VP -> V NP [0.6] | VP PP [0.4]
    PP -> P NP [1.0]
    Det -> 'the' [1.0]
    N -> 'dog' [0.9] | 'cat' [0.1]
    V -> 'chased' [1.0]
    P -> 'with' [1.0]
""")

# Create a parser with the PCNF
parser = nltk.ViterbiParser(pcnf_grammar)

# Define a new sentence to parse
sentence = "the dog chased the cat".split()

# Perform parsing
for tree in parser.parse(sentence):
    tree.pretty_print()
