# Jennifer Gamez
# Pregunta 2: Manejador de operaciones aritmeticas Pre-fijo y Post-fijo

def evaluate(expression, order):
    stack = []
    operators = {'+', '-', '*', '/'}

    if order == 'PRE':
        tokens = expression.split()[::-1]  # Invertir la expresión para trabajar con pre-fijo
    else:
        tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            op2 = stack.pop()
            op1 = stack.pop()
            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            elif token == '*':
                stack.append(op1 * op2)
            elif token == '/':
                if op2 != 0:
                    stack.append(op1 // op2) # División entera
                else:
                    print("Error: Division por cero.")
                    return None
    return stack[0]

def to_infix(expression, order):
    stack = []
    operators = {'+', '-', '*', '/'}

    if order == 'PRE':
        tokens = expression.split()[::-1]  # Invertir la expresión para trabajar con pre-fijo
    else:
        tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():
            stack.append(token)
        elif token in operators:
            op2 = stack.pop()
            op1 = stack.pop()

            if order == 'PRE':
                stack.append(f"({op1} {token} {op2})")
            else:
                stack.append(f"({op1} {token} {op2})")

    return stack[-1] if stack else None
