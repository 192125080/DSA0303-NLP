import nltk
from nltk import CFG, ChartParser

def check_agreement(sentence):
    grammar = CFG.fromstring("""
        S -> NP_SG VP_SG | NP_PL VP_PL
        NP_SG -> Det_SG N_SG | Det_SG N_PL
        NP_PL -> Det_PL N_PL
        VP_SG -> V_SG
        VP_PL -> V_PL
        Det_SG -> 'the'
        Det_PL -> 'the'
        N_SG -> 'dog' | 'cat'
        N_PL -> 'dogs' | 'cats'
        V_SG -> 'chases' | 'eats'
        V_PL -> 'chase' | 'eat'
    """)

    parser = ChartParser(grammar)
    tokens = sentence.split()
    try:
        for tree in parser.parse(tokens):
            return True
    except nltk.parse.api.ParseError:
        pass
    return False

def main():
    sentence = input("Enter a sentence: ")
    if check_agreement(sentence):
        print("The sentence follows the grammar.")
    else:
        print("The sentence does not follow the grammar.")

if __name__ == "__main__":
    main()
