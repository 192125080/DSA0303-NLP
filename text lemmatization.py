import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    lemmatized_text = ' '.join(lemmatized_words)
    return lemmatized_text

# Example usage
input_text = "I am running in the park and playing with my friends"
output_text = lemmatize_text(input_text)

print("Input Text:")
print(input_text)
print("\nOutput Text (after lemmatization):")
print(output_text)
