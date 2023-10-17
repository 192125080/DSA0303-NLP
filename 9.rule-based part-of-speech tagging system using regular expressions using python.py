import re

def rule_based_pos_tagging(text):
    # Define regular expressions for different parts of speech
    patterns = [
        (r'\b(?:run|jump|swim)\b', 'VB'),  # Verbs
        (r'\b(?:the|a|an)\b', 'DT'),      # Determiners
        (r'\b(?:quick|brown|lazy)\b', 'JJ'),  # Adjectives
        (r'\b(?:fox|dog)\b', 'NN'),       # Nouns
        (r'\b(?:over)\b', 'IN')           # Prepositions
    ]

    pos_tags = []

    for pattern, tag in patterns:
        matches = re.finditer(pattern, text, flags=re.IGNORECASE)
        for match in matches:
            pos_tags.append((match.group(), tag))

    return pos_tags

def main():
    user_input = input("Enter a sentence: ")

    tags = rule_based_pos_tagging(user_input)
    print(tags)

if __name__ == "__main__":
    main()
