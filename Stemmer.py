from nltk.stem import PorterStemmer

# Initialize the stemmer
stemmer = PorterStemmer()

# Define a list of words for stemming
words = ["running", "jumps", "played", "running"]

# Apply stemming
stemmed_words = [stemmer.stem(word) for word in words]

# Print the stemmed words
print(stemmed_words)
