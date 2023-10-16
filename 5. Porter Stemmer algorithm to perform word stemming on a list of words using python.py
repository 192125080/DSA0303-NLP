import nltk
from nltk.stem import PorterStemmer

def stem_words(words):
    porter_stemmer = PorterStemmer()
    stemmed_words = [porter_stemmer.stem(word) for word in words]
    return stemmed_words

def main():
    words = ['running', 'jumps', 'jumping', 'easily', 'quickly', 'foxes']

    stemmed_words = stem_words(words)

    print("Original Words\tStemmed Words")
    print("---------------------------------")
    for word, stemmed_word in zip(words, stemmed_words):
        print(f"{word}\t\t{stemmed_word}")

if __name__ == "__main__":
    main()
