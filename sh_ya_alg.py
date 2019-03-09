import re


def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_name(string):
    return re.match("\w+", string)


def peek(stack):
    return stack[-1] if stack else None


def greater_precedence(op1, op2):
    precedences = {'(': -1, '=': 0, '+': 1, '-': 1, '*': 2, '/': 2, '**': 3}
    return precedences[op1] > precedences[op2] or precedences[op1] == precedences[op2]


def print_stack(stack):
    print('-'*20)
    print("Stack: \n")
    for i in reversed(stack):
        print('|', i, '|')
    print('_'*5)


def reverse(expression):
    tokens = re.findall("[=+/*()-]|\d+", expression)
    result = []
    stack = []
    for token in tokens:
        if is_number(token):
            result.append(token)
            print_stack(stack)
            print("Result: ", result)
        elif token == '(':
            stack.append(token)
            print_stack(stack)
            print("Result: ", result)
        elif token == ')':
            top = peek(stack)
            while top is not None and top != '(':
                result.append(stack.pop())
                top = peek(stack)
                print_stack(stack)
                print("Result: ", result)
            stack.pop()
        else:
            top = peek(stack)
            while top is not None and greater_precedence(top, token):
                result.append(stack.pop())
                top = peek(stack)
                print_stack(stack)
                print("Result: ", result)
            stack.append(token)
    while peek(stack) is not None:
        result.append(stack.pop())
        print_stack(stack)
        print("Result: ", result)

    return result
