import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a list of words for lemmatization
words = ["running", "jumps", "played", "running"]

# Apply lemmatization
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Print the lemmatized words
print(lemmatized_words)
