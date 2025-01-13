def postfixEval(postfixExpr):
    stack = []

    for token in postfixExpr.split():
        if token.isdigit():  # Check if the token is a digit
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
            elif token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
    
    return stack[0]  # Return the final result

# Example usage
print(postfixEval('2 3 4 * + 6 - '))  # Output: 20
