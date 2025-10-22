import Cos, Cot, Csc, Factorial, Ln, Log, nCr, nPr, Onto, S, Sec, Sin, Tan, math

def read_number(postfix, i):
    start = i
    while i < len(postfix) and postfix[i].isdigit() or postfix[i] == '.':
        i += 1
    return float(postfix[start:i]), i

def calculate_postfix(postfix):
    stack = []
    i = 0
    while i < len(postfix):
        ch = postfix[i]
        if ch.isdigit():
            number, i = read_number(postfix, i)
            stack.append(number)
            continue
        else:
            match ch:
                case 'u': # negative
                    if i + 5 < len(postfix) and postfix[i+1:i+6] == 'nary-':
                        stack[len(stack) -  1] *= -1
                        i += 5
                case '+': # addition
                    stack.append(float(stack.pop() + stack.pop()))
                case '-': # subtraction
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(float(b - a))
                case '*': # multiplication
                    stack.append(float(stack.pop() * stack.pop()))
                case '/': # division
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(float(b / a))
                case '%': # modulo
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b % a)
                case '^': # power
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b ** a)
                case '!':
                    stack.append(float(Factorial.calculate_factorial(int(stack.pop()))))
                case 'S': # Stirling numbers
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(float(S.calculate_s(b, a)))
                case 's': # sin, sec, sqrt
                    if i + 2 < len(postfix):
                        if postfix[i + 1] == 'i' and postfix[i + 2] == 'n':
                            stack.append(float(Sin.calculate_sin(int(stack.pop()))))
                            i += 2
                        elif postfix[i + 1] == 'e' and postfix[i + 2] == 'c':
                            stack.append(float(Sec.calculate_sec(int(stack.pop()))))
                            i += 2
                    if i + 3 < len(postfix) and postfix[i + 1] == 'q' and postfix[i + 2] == 'r' and postfix[i + 3] == 't':
                        if stack[len(stack) - 1] < 0:
                            return f'sorry cannot calculate **sqrt({stack[len(stack) - 1]})**, we will make it soon!'
                        stack.append(float(math.sqrt(stack.pop())))
                        i += 3
                case 'c': # cos, cot, csc, ceil
                    if i + 2 < len(postfix):
                        if postfix[i + 1] == 'o' and postfix[i + 2] == 's':
                            stack.append(float(Cos.calculate_cos(int(stack.pop()))))
                            i += 2
                        elif postfix[i + 1] == 'o' and postfix[i + 2] == 't':
                            stack.append(float(Cot.calculate_cot(int(stack.pop()))))
                            i += 2
                        elif postfix[i + 1] == 's' and postfix[i + 2] == 'c':
                            stack.append(float(Csc.calculate_csc(int(stack.pop()))))
                            i += 2
                    if i + 3 < len(postfix) and postfix[i+1:i+4] == 'eil':
                        stack.append(math.ceil(stack.pop()))
                        i += 3
                case 't': # tan
                    if i + 2 < len(postfix) and postfix[i + 1] == 'a' and postfix[i + 2] == 'n':
                        stack.append(float(Tan.calculate_tan(int(stack.pop()))))
                        i += 2
                case 'P': # nPr
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(float(nPr.calculate_npr(b, a)))
                case 'C': # nCr
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(float(nCr.calculate_ncr(b, a)))
                case 'O': # Onto functions
                    if i + 3 < len(postfix) and postfix[i+1:i+3] == 'nto':
                        a = int(stack.pop())
                        b = int(stack.pop())
                        stack.append(float(Onto.calculate_onto(b, a)))
                        i += 3
                case 'l': # ln, log
                    if i + 1 < len(postfix) and postfix[i + 1] == 'n':
                        i += 1
                        a = float(stack.pop())
                        stack.append(float(Ln.calculate_ln(a)))
                    elif i + 2 < len(postfix) and postfix[i + 1] == 'o' and postfix[i + 2] == 'g':
                        i += 2
                        base = 10
                        if i + 1 < len(postfix) and postfix[i + 1].isdigit():
                            i += 1
                            base = int(postfix[i])
                            while i + 1 < len(postfix) and postfix[i + 1].isdigit():
                                i += 1
                                base = base * 10 + int(postfix[i])
                        a = float(stack.pop())
                        stack.append(float(Log.calculate_log(base, a)))
                case 'f': # floor
                    if i + 4 < len(postfix) and postfix[i:i+5] == 'floor':
                        stack.append(math.floor(stack.pop()))
                        i += 4
        i += 1
    return stack.pop()