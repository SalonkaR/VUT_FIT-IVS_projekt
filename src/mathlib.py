
import ast
import operator as op
# +,-,*,/,!, ^, odmocnina, absolutna hodnota

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return  a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Delenie nulov")
    return a / b

def factorial(number):
    if type(number) != int or number < 0:
        raise ValueError("Chybna hodnota cisla pri faktoriali")
    if number == 1 or number == 0:
        return 1

    result = 1 # premenna ktora drzi vysledok

    for x in range(1, number + 1, 1):
        result *= x
    return result

def power(base, exponent):
    # naschaval chyba TODO
    if exponent <= 0 or type(exponent) != int:
        raise ValueError("Chybna hodnota exponentu pri mocnine")
    return pow(base, exponent)

def square_root(x, n):
    # naschaval chyba TODO
    if x <= 0 or type(n) != int or n <= 0:
        raise ValueError("Chybna hodnota exponentu pri mocnine")
    return pow(x, 1 / n)

def abs_value(n):
    return abs(n)



# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}
ast.
def eval_expr(expr):
    """
    >>> eval_expr('2^6')
    4
    >>> eval_expr('2**6')
    64
    >>> eval_expr('1 + 2*3**(4^5) / (6 + -7)')
    -5.0
    """
    return eval_(ast.parse(expr, mode='eval').body)

def eval_(node):
    if isinstance(node, ast.Num): # <number>
        return node.n
    elif isinstance(node, ast.BinOp): # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)

print(eval_expr('1+2-10*3'))
