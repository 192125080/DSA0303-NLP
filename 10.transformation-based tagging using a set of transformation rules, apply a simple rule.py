def transform_based_tagging(text):
    rules = {
        'run': 'VB',
        'jump': 'VB',
        'swim': 'VB',
        'the': 'DT',
        'a': 'DT',
        'an': 'DT',
        'quick': 'JJ',
        'brown': 'JJ',
        'lazy': 'JJ',
        'fox': 'NN',
        'dog': 'NN',
        'over': 'IN'
    }

    tagged_text = []

    for word in text.split():
        tagged_text.append((word, rules.get(word.lower(), 'NN')))

    return tagged_text

def main():
    user_input = input("Enter a sentence: ")

    tagged_text = transform_based_tagging(user_input)
    print(tagged_text)

if __name__ == "__main__":
    main()
