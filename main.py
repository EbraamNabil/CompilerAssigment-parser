class RecursiveDescentParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        self.current_token_index = 0
        if self.E() and self.current_token_index == len(self.tokens):
            print("Parsing successful!")
        else:
            print("Parsing failed.")

    def match(self, expected_token):
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index] == expected_token:
            self.current_token_index += 1
            return True
        return False

    def E(self):
        # E → T E'
        print("Enter E")
        if self.T():
            if self.E_prime():
                print("Exit E")
                return True
        print("Exit E (failed)")
        return False

    def E_prime(self):
        # E' → + T E' | ε
        print("Enter E'")
        if self.match('+'):
            if self.T():
                if self.E_prime():
                    print("Exit E'")
                    return True
            print("Exit E' (failed)")
            return False
        # ε (do nothing)
        print("Exit E' (ε)")
        return True

    def T(self):
        # T → F T'
        print("Enter T")
        if self.F():
            if self.T_prime():
                print("Exit T")
                return True
        print("Exit T (failed)")
        return False

    def T_prime(self):
        # T' → * F T' | ε
        print("Enter T'")
        if self.match('*'):
            if self.F():
                if self.T_prime():
                    print("Exit T'")
                    return True
            print("Exit T' (failed)")
            return False
        # ε (do nothing)
        print("Exit T' (ε)")
        return True

    def F(self):
        # F → ( E ) | id
        print("Enter F")
        if self.match('('):
            if self.E():
                if self.match(')'):
                    print("Exit F")
                    return True
            print("Exit F (failed)")
            return False
        elif self.match('id'):
            print("Exit F")
            return True
        print("Exit F (failed)")
        return False


# Example Usage
def main():
    # Input string to parse
    input_expression = "( id + id ) * id"
    tokens = input_expression.split()

    # Create parser instance and parse
    parser = RecursiveDescentParser(tokens)
    parser.parse()

if __name__ == "__main__":
    main()
