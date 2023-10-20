import nltk

def recognize_dialog_acts(text):
    sentences = nltk.sent_tokenize(text)
    dialog_acts = []
    
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        tagged_tokens = nltk.pos_tag(tokens)
        
        # Identify common patterns for dialog acts
        if tagged_tokens[0][1] == 'PRP' and tagged_tokens[1][1] == 'VBP':
            dialog_acts.append(('Statement', sentence))
        elif tagged_tokens[0][1] == 'WP' or tagged_tokens[0][1] == 'WRB':
            dialog_acts.append(('Question', sentence))
        else:
            dialog_acts.append(('Other', sentence))
    
    return dialog_acts

if __name__ == '__main__':
    dialog = """
    John: Hi, how are you doing?
    Mary: I'm good, thanks! How about you?
    John: I'm doing well too. Did you enjoy the movie?
    Mary: Yes, it was great!
    """
    
    dialog_acts = recognize_dialog_acts(dialog)
    
    for act, sentence in dialog_acts:
        print(f"Dialog Act: {act}\nSentence: {sentence}\n")
