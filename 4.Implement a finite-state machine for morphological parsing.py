import re

class PluralizationFSM:
    def __init__(self):
        self.irregular_nouns = {
            "child": "children",
            "woman": "women",
            "man": "men",
        }
        self.rules = [
            (r'^(.*?)(s|x|sh|ch)$', r'\1\2es'),  # Words ending in s, x, sh, or ch become 'es'
            (r'^(.*?[aeiouAEIOU])y$', r'\1ies'),  # Words ending in 'y' after a vowel become 'ies'
            (r'^(.*?[^aeiouAEIOU])y$', r'\1ys'),  # Words ending in 'y' after a consonant become 'ys'
            (r'^(.*?)$', r'\1s'),  # Default rule: add 's'
        ]

    def pluralize(self, noun):
        if noun in self.irregular_nouns:
            return self.irregular_nouns[noun]

        for pattern, replacement in self.rules:
            if re.match(pattern, noun):
                return re.sub(pattern, replacement, noun)

def main():
    pluralizer = PluralizationFSM()

    while True:
        noun = input("Enter a singular noun (or 'exit' to quit): ")
        
        if noun.lower() == 'exit':
            break

        plural = pluralizer.pluralize(noun)
        print(f"The plural form of '{noun}' is '{plural}'.")

if __name__ == "__main__":
    main()
