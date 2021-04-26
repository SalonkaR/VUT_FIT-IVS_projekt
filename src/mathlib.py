## 
# @package
# Mathlib je kniznica pre kalkulacku
#
# V kniznici sa nachadzaju matematicke operacie pre pracu na kalkulacke
# Taktiez sa v tejto kniznici nachadza funkcia solve_expr, ktora spracuje vyraz
# a vrati vysledok na zobrazenie
# @file mathlib.py
# @date 24.4.2021






import re

##
# @brief Spocita dve cisla dokopy
# @param a prvy operand
# @param b druhy operand
# @return soucet cisiel "a" a "b"
def add(a, b):
    return a + b

##
# @brief Odpocita dve cisla 
# @param a prvy operand
# @param b druhy operand
# @return rozdiel cisiel "a" a "b"
def minus(a, b):
    return a - b

##
# @brief Vynasobi dve cisla 
# @param a prvy operand
# @param b druhy operand
# @return nasobok cisiel "a" a "b"
def multiply(a, b):
    return  a * b

##
# @brief Vydeli dve cisla 
# @param a prvy operand
# @param b druhy operand
# @exception Delenie nulob ak druhy operand sa bude rovnat nule
# @return Vydeli cislo "a" cislom "b"
def divide(a, b):
    if b == 0:
        raise ValueError("Delenie nulov")
    return a / b

##
# @brief Vypocita faktorial zo zadaneho cisla
# @param number zadane cislo pre vypocet faktorialu
# @exception ValueError ak bude zla hodnota number
# @return faktorial cisla 
def factorial(number):
    if type(number) != int or number < 0:
        raise ValueError("Chybna hodnota cisla pri faktoriali")
    if number == 1 or number == 0:
        return 1

    result = 1 # premenna ktora drzi vysledok

    for x in range(1, number + 1, 1):
        result *= x
    return result

##
# @brief Umocni dane cislo s danym exponentom 
# @param base zaklad mocniny
# @param exponent exponent mocniny
# @return umocneho cislo "base na exponent"
def power(base, exponent):
    if exponent < 0 and base < 0:
        return -(base**exponent)
    return base**exponent

##
# @brief Vypocita n tu odmocninu z cisla x
# @param x odmocnenec
# @param n n-ta odmocnina
# @exception ValueError v pripade ak boli zle zadane hodnoty na odmocnenie
# @return odmocnene cislo
def square_root(x, n):
    if n == 0:
        raise ValueError("Chybna hodnota exponentu pri mocnine")
    if (n % 2 == 0 and x < 0):
        raise ValueError("Chybna hodnota exponentu pri mocnine")
    if n % 2 != 0 and x < 0:
        return - abs(x)**(1/n)
    return x**(1/n)

##
# @brief Vypocita absolutnu hodnotu cisla
# @param n zadane cislo
# @return absolutna hodnota cisla n
def abs_value(n):
    return abs(n)

##
# @brief Zameni v retazci absolutne hodnoty za vypocitanu hodnotu
# @param expr retazec s vyrazom
# @return retazec s vypocitanimi asbolutnimi hodnotami
def replace_abs(expr):
    regex_abs = r'(abs([+-]?([0-9]+[.])?[0-9]+))'
    matches = re.findall(regex_abs, expr)
    for match in matches:
        expr = expr.replace(match[0], str(abs_value(float(match[1]))))
    return expr

##
# @brief Zameni v retazci faktoriali za vypocitanu hodnotu
# @param expr retazec s vyrazom
# @return retazec s vypocitanimi faktorialmi
def replace_fac(expr):
    regex_abs = r'(fac([0-9]+))'
    matches = re.findall(regex_abs, expr)
    for match in matches:
        expr = expr.replace(match[0], str(factorial(int(match[1]))))
    return expr

##
# @brief Zameni v retazci odmocniny za vypocitanu hodnotu
# @param expr retazec s vyrazom
# @return retazec s vypocitanimi odmocninami 
def replace_root(expr):
    regex_root = r'(([0-9])+[√](([+-]?[0-9]+[.])?[+-]?[0-9]+))'
    matches = re.findall(regex_root, expr)
    for match in matches:
        expr = expr.replace(match[0], str(square_root(float(match[2]), int(match[1]))))
    return expr

##
# @brief Zameni v retazci mocniny za vypocitanu hodnotu
# @param expr retazec s vyrazom
# @return retazec s vypocitanimi mocninami 
def replace_power(expr):
    regex_power = r'((([0-9]+[.])?[0-9]+)[\^](([+-]?[0-9]+[.])?[+-]?[0-9]+))'
    matches = re.findall(regex_power, expr)
    for match in matches:
        expr = expr.replace(match[0], str(power(float(match[1]), float(match[3]))))
    return expr

##
# Funkcia skontroluje syntax vyrazu bez zavoriek a vyhodnoti dany vyraz a vrati vysledok
# 
# @param expr retazec s vyrazom
# @exception ValueError v pripade ak vyraz je syntakticky zle zadany
# @return vyhodnoteni retazec
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


##
# Funkcia skontroluje syntax vyrazu a vyhodnoti dany vyraz a vrati vysledok
# 
# @param expr retazec s vyrazom
# @exception ValueError v pripade ak vyraz je syntakticky zle zadany
# @return vyhodnoteni retazec
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
