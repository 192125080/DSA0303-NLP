class FSA:
    def __init__(self):
        self.current_state = 0

    def transition(self, input_char):
        if self.current_state == 0:
            if input_char == 'a':
                self.current_state = 1
            else:
                self.current_state = 0
        elif self.current_state == 1:
            if input_char == 'b':
                self.current_state = 2
            elif input_char == 'a':
                self.current_state = 1
            else:
                self.current_state = 0
        elif self.current_state == 2:
            if input_char == 'a':
                self.current_state = 1
            else:
                self.current_state = 0

    def is_accepted(self):
        return self.current_state == 2


def match_pattern(input_string):
    fsa = FSA()

    for char in input_string:
        fsa.transition(char)

    return fsa.is_accepted()


# Testing the automaton
test_strings = ["ab", "aab", "bab", "aaab", "ba", "b"]
for test_str in test_strings:
    if match_pattern(test_str):
        print(f"'{test_str}' matches the pattern.")
    else:
        print(f"'{test_str}' does not match the pattern.")
