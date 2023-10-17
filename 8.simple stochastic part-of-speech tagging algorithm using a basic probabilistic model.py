import random

def stochastic_pos_tagging(text):
    words = text.split()
    pos_tags = []
    
    for word in words:
        # Generate a random part-of-speech tag for each word
        pos_tag = random.choice(['NN', 'VB', 'JJ', 'DT'])  # Simplified POS tags for demonstration
        pos_tags.append((word, pos_tag))
    
    return pos_tags

def main():
    user_input = input("Enter a sentence: ")

    tags = stochastic_pos_tagging(user_input)
    print(tags)

if __name__ == "__main__":
    main()
