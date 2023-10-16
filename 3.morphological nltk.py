import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('wordnet')

def perform_morphological_analysis(sentence):
    tokens = word_tokenize(sentence)
    analysis = []

    for token in tokens:
        synsets = wordnet.synsets(token)
        if synsets:
            lemma = synsets[0].lemmas()[0].name()
            analysis.append((token, lemma))
        else:
            analysis.append((token, None))

    return analysis

def main():
    sentence = "The quick brown fox jumps over the lazy dog"
    morphological_analysis = perform_morphological_analysis(sentence)

    print("Original Token\t\tLemmatized Form")
    print("----------------------------------------")
    for token, lemma in morphological_analysis:
        print(f"{token}\t\t\t{lemma if lemma else 'N/A'}")

if __name__ == "__main__":
    main()
