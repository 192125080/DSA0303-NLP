import nltk
from nltk.parse.corenlp import CoreNLPParser
from nltk.tree import ParentedTree

# Initialize the Stanford CoreNLP parser
parser = CoreNLPParser(url="http://localhost:9000")

# Sample text
sample_text = "Although it was raining, John went for a walk. He enjoyed the fresh air and the sound of raindrops."

# Tokenize and parse the text
sentences = list(parser.raw_parse(sample_text))

# Function to traverse and print discourse relations
def traverse_tree(tree, level=0):
    if isinstance(tree, ParentedTree):
        print("  " * level + tree.label())
        for subtree in tree:
            traverse_tree(subtree, level + 1)

# Analyze and print discourse structure
for sentence_tree in sentences:
    traverse_tree(sentence_tree)

# Close the CoreNLP server
parser.api_call("shutdown")
