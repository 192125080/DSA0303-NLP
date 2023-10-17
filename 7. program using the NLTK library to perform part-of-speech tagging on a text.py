import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Perform part-of-speech tagging
    pos_tags = pos_tag(words)
    
    return pos_tags

def main():
    user_input = input("Enter a sentence: ")

    tags = pos_tagging(user_input)
    print(tags)

if __name__ == "__main__":
    main()
