
import re

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
    if exponent < 0 and base < 0:
        return -(base**exponent)
    return base**exponent


def square_root(x, n):
    if n == 0:
        raise ValueError("Chybna hodnota exponentu pri mocnine")
    if (n % 2 == 0 and x < 0):
        raise ValueError("Chybna hodnota exponentu pri mocnine")
    if n % 2 != 0 and x < 0:
        return - abs(x)**(1/n)
    return x**(1/n)

def abs_value(n):
    return abs(n)

def replace_abs(expr):
    regex_abs = r'(abs([+-]?([0-9]+[.])?[0-9]+))'
    matches = re.findall(regex_abs, expr)
    for match in matches:
        expr = expr.replace(match[0], str(abs_value(float(match[1]))))
    return expr

def replace_fac(expr):
    regex_abs = r'(fac([0-9]+))'
    matches = re.findall(regex_abs, expr)
    for match in matches:
        expr = expr.replace(match[0], str(factorial(int(match[1]))))
    return expr

def replace_root(expr):
    regex_root = r'(([0-9])+[√](([+-]?[0-9]+[.])?[+-]?[0-9]+))'
    matches = re.findall(regex_root, expr)
    for match in matches:
        expr = expr.replace(match[0], str(square_root(float(match[2]), int(match[1]))))
    return expr

def replace_power(expr):
    regex_power = r'((([0-9]+[.])?[0-9]+)[\^](([+-]?[0-9]+[.])?[+-]?[0-9]+))'
    matches = re.findall(regex_power, expr)
    for match in matches:
        expr = expr.replace(match[0], str(power(float(match[1]), float(match[3]))))
    return expr

def solve_expr_no_brack(expr):
    if "," in expr:
        raise ValueError("Treba pouzit bodku miesto ciarky")
    # chyby zadania napr "abs120." alebo "fac2.2"
    if re.search(r'(fac([0-9]+\.))', expr):
        raise ValueError("Zle zadana syntax pri faktoriali")
    if re.search(r'abs([+-])?[0-9]+\.[^0-9]', expr) or re.search(r'abs([+-])?[0-9]+\.$',expr):
        raise ValueError("Zle zadana syntax pri absolutnej hodnotne")
    if re.search(r'([0-9]+[√][+-]?[0-9]+[.][^0-9])', expr) or re.search(r'([0-9]+[√][+-]?[0-9]+[.]$)', expr):
        raise ValueError("Zle zadana syntax pri odmocnine")


    expr = replace_abs(expr)
    expr = replace_fac(expr)
    expr = replace_root(expr)
    expr = replace_power(expr)
    if "^" in expr:
        raise ValueError("Zla syntax mocniny")
    try:
        expr = eval(expr)
    except Exception:
        raise ValueError("Zla syntax") from None
    if type(expr) != int and type(expr) != float and type(expr) != str:
        raise ValueError("Zla syntax 1")
    if int(expr) != expr:
        return float(expr)
    else:
        return int(expr)


def solve_expr(expr):
    left_brack = len(re.findall("\(", expr))
    right_brack = len(re.findall("\)", expr))

    if (left_brack != right_brack):
        raise ValueError("Zly pocet zatvoriek")

    while (len(re.findall("\(", expr)) > 0):
        regex_brack = r'\(([^\(\)]*)\)'
        matches = re.findall(regex_brack, expr)

        for match in matches:
            sub_expr = "(" + match + ")"
            expr = expr.replace(sub_expr, str(solve_expr_no_brack(match)))

    return solve_expr_no_brack(expr)
