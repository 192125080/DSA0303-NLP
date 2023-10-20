import nltk

def text_coherence(text):
    sentences = nltk.sent_tokenize(text)
    total_distance = 0
    total_words = 0
    
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        total_words += len(tokens)
        total_distance += len(tokens) - 1
    
    coherence = total_distance / total_words if total_words > 0 else 0
    return coherence

if __name__ == '__main__':
    text = """
    John met Mary. She gave him a book. He thanked her.
    """
    
    coherence_score = text_coherence(text)
    
    print(f"Coherence Score: {coherence_score}")
