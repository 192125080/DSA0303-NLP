import random

def generate_bigram_model(text):
    words = text.split()
    bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
    model = {}
    for word1, word2 in bigrams:
        if word1 not in model:
            model[word1] = []
        model[word1].append(word2)
    return model

def generate_text_bigram(model, seed_word, num_words):
    current_word = seed_word
    generated_text = [current_word]
    for _ in range(num_words-1):
        next_word = random.choice(model.get(current_word, []))
        if next_word is None:
            break
        generated_text.append(next_word)
        current_word = next_word
    return ' '.join(generated_text)

def main():
    corpus = input("Enter a corpus: ")
    seed_word = input("Enter a seed word: ")
    num_words = int(input("Enter the number of words to generate: "))

    model = generate_bigram_model(corpus)

    generated_text = generate_text_bigram(model, seed_word, num_words)
    print(generated_text)

if __name__ == "__main__":
    main()
