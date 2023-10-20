import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag

def resolve_references(text):
    sentences = sent_tokenize(text)
    resolved_text = ""
    reference_dict = {}
    
    for sentence in sentences:
        tokens = word_tokenize(sentence)
        tagged_tokens = pos_tag(tokens)
        
        for i in range(len(tagged_tokens)):
            word, pos = tagged_tokens[i]
            
            if pos in ['PRP', 'PRP$', 'WP', 'WP$']:
                if i > 0 and tagged_tokens[i-1][0].istitle():
                    antecedent = tagged_tokens[i-1][0]
                    reference_dict[word] = antecedent
                    resolved_text += antecedent + ' '
                else:
                    resolved_text += word + ' '
            else:
                resolved_text += word + ' '
        
        resolved_text += ' '

    return resolved_text.strip(), reference_dict

if __name__ == '__main__':
    text = """
    John met Mary. She gave him a book. He thanked her.
    """

    resolved_text, reference_dict = resolve_references(text)

    print("Resolved Text:")
    print(resolved_text)

    print("\nReference Dictionary:")
    for pronoun, antecedent in reference_dict.items():
        print(f"'{pronoun}' refers to '{antecedent}'")
