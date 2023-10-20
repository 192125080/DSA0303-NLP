import spacy

def extract_noun_phrases(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    return noun_phrases

def get_meaning(noun_phrase):
    meanings = {
        'cat': 'a small domesticated carnivorous mammal',
        'book': 'a written or printed work consisting of pages glued or sewn together',
        'John Doe': 'a placeholder name for an unidentified person'
        # Add more meanings as needed
    }
    return meanings.get(noun_phrase, 'Meaning not found')

if __name__ == '__main__':
    sentence = "John Doe has a cat and a book."
    
    noun_phrases = extract_noun_phrases(sentence)
    
    if noun_phrases:
        for np in noun_phrases:
            meaning = get_meaning(np)
            print(f'Noun Phrase: "{np}", Meaning: {meaning}')
    else:
        print("No noun phrases found.")
