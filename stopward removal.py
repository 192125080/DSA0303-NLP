import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def remove_stopwords(text):
    # Tokenize the input text
    words = nltk.word_tokenize(text)
    
    # Get the list of English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Filter out the stopwords from the text
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Reconstruct the text without stopwords
    filtered_text = ' '.join(filtered_words)
    
    return filtered_text

# Example usage
input_text = "This is an example sentence with some stopwords that need to be removed."
output_text = remove_stopwords(input_text)

print("Input Text:")
print(input_text)
print("\nOutput Text (after stopwords removal):")
print(output_text)
