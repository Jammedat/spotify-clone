def postfixEval(exp):
    operators = {'+', '-', '*', '/', '**'}  # Define valid operators
    stack = []

    for token in exp.split():
        if token not in operators:  # If the token is not an operator, treat it as an operand
            stack.append(int(token))  # Push the operand onto the stack
        else:  # If the token is an operator
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
                
            elif token == '**':  
                
                stack.append(a ** b)

    return stack[0]  # Return the final result

# Example usage
print(postfixEval('1 2 + 3 * 4 3 - - 2 1 + **'))  # Output: 20
