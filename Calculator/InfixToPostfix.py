import re

PRECEDENCE = {
    '+': 1, '-': 1,
    '*': 2, '/': 2, '%': 2,
    'P': 2, 'C': 2,
    '^': 3, 'unary-': 4,
    '!': 5
}

ASSOCIATIVITY = {
    '+': 0, '-': 0,
    '*': 0, '/': 0, '%': 0,
    'P': 0, 'C': 0,
    '!': 0, '^': 1,
    'unary-': 1
}


def is_number(token):
    return re.match(r'-?\d+(\.\d+)?$', token) is not None


def is_operator(token):
    return token in PRECEDENCE


def is_function(token):
    return re.match(r'[a-zA-Z]+', token) or re.match(r'log\d+.*', token)


def compare_operators(op1, op2):
    return PRECEDENCE[op1] - PRECEDENCE[op2]


def get_associativity(op):
    return ASSOCIATIVITY.get(op, 0)


def infix_to_postfix(infix):
    output = []
    stack = []
    tokenizer = Tokenizer(infix)
    prev_token = None

    while tokenizer.has_next():
        token = tokenizer.next()

        if token == "calc":
            if stack and is_operator(stack[-1]):
                output.append(stack.pop())
        elif is_number(token):
            output.append(token)
        elif is_function(token):
            stack.append(token)
        elif is_operator(token):
            if token == "-" and (prev_token is None or prev_token == "(" or is_operator(prev_token)):
                token = "unary-"
            while stack and is_operator(stack[-1]):
                top_op = stack[-1]
                cmp = compare_operators(top_op, token)
                if cmp > 0 or (cmp == 0 and get_associativity(token) == 0):
                    output.append(stack.pop())
                else:
                    break
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if not stack:
                raise RuntimeError("Mismatched parentheses")
            stack.pop()
            if stack and is_function(stack[-1]):
                output.append(stack.pop())
        elif token == "|" and stack.count("|") == 0:
            stack.append(token)
        elif token == "|" and stack.count("|") == 1:
            while stack and stack[-1] != "|":
                output.append(stack.pop())
            if not stack:
                raise RuntimeError("| is missing.")
            stack.pop()
            output.append('|')
            if stack and is_function(stack[-1]):
                output.append(stack.pop())
        else:
            raise RuntimeError(f"Invalid token: {token}")

        prev_token = token

    while stack:
        if stack[-1] == "(":
            raise RuntimeError("Mismatched parentheses")
        output.append(stack.pop())

    return " ".join(output)


class Tokenizer:
    def __init__(self, input_str):
        self.input = re.sub(r'\s+', '', input_str)
        self.pos = 0

    def has_next(self):
        return self.pos < len(self.input)

    def next(self):
        if self.pos >= len(self.input):
            return None

        c = self.input[self.pos]
        if c == ',':
            self.pos += 1
            return "calc"
        elif c.isdigit() or c == '.':
            return self.read_number()
        elif c.isalpha():
            return self.read_function()
        elif c in "()":
            self.pos += 1
            return c
        else:
            self.pos += 1
            return c

    def read_number(self):
        start = self.pos
        while self.pos < len(self.input) and (self.input[self.pos].isdigit() or self.input[self.pos] == '.'):
            self.pos += 1
        return self.input[start:self.pos]

    def read_function(self):
        start = self.pos
        while self.pos < len(self.input) and self.input[self.pos].isalpha():
            self.pos += 1
        if self.input[start:self.pos] == "log":
            while self.pos < len(self.input) and self.input[self.pos].isdigit():
                self.pos += 1
        return self.input[start:self.pos]