import nltk

# Download necessary resources

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')



def get_parts_of_speech(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    return pos_tags

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
parts_of_speech = get_parts_of_speech(sentence)

for word, pos in parts_of_speech:
    print(f"{word}: {pos}")
