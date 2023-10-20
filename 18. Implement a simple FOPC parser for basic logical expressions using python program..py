,class FOPCParser:
    def __init__(self):
        self.variables = set()
        self.predicates = set()

    def parse(self, expression):
        self.variables.clear()
        self.predicates.clear()
        return self.parse_expression(expression)

    def parse_expression(self, expression):
        expression = expression.replace(" ", "")
        if expression[0] == '(' and expression[-1] == ')':
            return self.parse_expression(expression[1:-1])
        elif expression[0] == '~':
            return not self.parse_expression(expression[1:])
        elif any(operator in expression for operator in ['∧', '∨', '→', '↔']):
            for operator in ['∧', '∨', '→', '↔']:
                parts = expression.split(operator, 1)
                if len(parts) == 2:
                    left = self.parse_expression(parts[0])
                    right = self.parse_expression(parts[1])
                    return self.apply_operator(operator, left, right)
        elif expression[0] == '∀' or expression[0] == '∃':
            quantifier, rest = expression[0], expression[1:]
            variable, rest = rest[0], rest[1:]
            self.variables.add(variable)
            return self.parse_quantifier(quantifier, variable, rest)
        elif re.match(r'^[A-Z][a-z]*\([^)]+\)$', expression):
            self.predicates.add(expression.split('(', 1)[0])
            return True
        else:
            raise SyntaxError("Invalid expression")

    def parse_quantifier(self, quantifier, variable, expression):
        return self.parse_expression(expression)  # Placeholder for handling quantifiers

    def apply_operator(self, operator, left, right):
        if operator == '∧':
            return left and right
        elif operator == '∨':
            return left or right
        elif operator == '→':
            return (not left) or right
        elif operator == '↔':
            return left == right

# Example usage
if __name__ == "__main__":
    parser = FOPCParser()

    expression = "P(x) ∧ Q(y)"
    result = parser.parse(expression)
    print(f"The result of '{expression}' is: {result}")

    expression = "∀x (P(x) ∨ Q(x))"
    result = parser.parse(expression)
    print(f"The result of '{expression}' is: {result}")

    print("Variables:", parser.variables)
    print("Predicates:", parser.predicates)
