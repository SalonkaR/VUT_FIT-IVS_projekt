import unittest
#from mathlib import add, minus, multiply, divide, factorial, power, square_root, abs_value

class addTests(unittest.TestCase):

    def test_add1(self):
        self.assertEqual(add(3,3), 6, "Ma byt 6")
    def test_add2(self):
        self.assertEqual(add(-2,5), 3, "Ma byt 3")
    def test_add3(self):
        self.assertEqual(add(1,-1), 0, "Ma byt 0")
    def test_add4(self):
        self.assertEqual(add(10,100), 110, "Ma byt 110")
    def test_add5(self):
        self.assertEqual(add(0,0), 0, "Ma byt 0")
    def test_add6(self):
        self.assertEqual(add(-2,-2), -4, "Ma byt -4")
    def test_add7(self):
        self.assertEqual(add(0.5,0.1), 0.6, "Ma byt 0.6")

class minusTests(unittest.TestCase):
    def test_minus1(self):
        self.assertEqual(minus(4,3), 1, "Ma byt 1")
    def test_minus2(self):
        self.assertEqual(minus(-2,5), -7, "Ma byt -7")
    def test_minus3(self):
        self.assertEqual(minus(1,-1), 2, "Ma byt 2")
    def test_minus4(self):
        self.assertEqual(minus(10,100), -90, "Ma byt -90")
    def test_minus5(self):
        self.assertEqual(minus(0,0), 0, "Ma byt 0")
    def test_minus6(self):
        self.assertEqual(minus(-2,-2), 0, "Ma byt 0")
    def test_minus7(self):
        self.assertEqual(minus(0.7,0.05), 0.65, "Ma byt 0.65")

class multipyTests(unittest.TestCase):
    def test_multiply1(self):
        self.assertEqual(multiply(4,3), 12, "Ma byt 12")
    def test_multiply2(self):
        self.assertEqual(multiply(-2,5), -10, "Ma byt -10")
    def test_multiply3(self):
        self.assertEqual(multiply(1,-1), -1, "Ma byt -1")
    def test_multiply4(self):
        self.assertEqual(multiply(10,100), 1000, "Ma byt 1000")
    def test_multiply5(self):
        self.assertEqual(multiply(5,0), 0, "Ma byt 0")
    def test_multiply6(self):
        self.assertEqual(multiply(-2,-2), 4, "Ma byt 4")
    def test_multiply7(self):
        self.assertEqual(divide(10,0.5), 5, "Ma byt 5")

class divideTests(unittest.TestCase):
    def test_divide1(self):
        self.assertEqual(divide(6,3), 2, "Ma byt 2")
    def test_divide2(self):
        self.assertEqual(divide(-30,5), -6, "Ma byt -6")
    def test_divide3(self):
        self.assertEqual(divide(1,-1), -1, "Ma byt -1")
    def test_divide4(self):
        self.assertEqual(divide(10,100), 0.1, "Ma byt 0.1")
    def test_divide5(self):
        self.assertRaises(ValueError, divide(5,0),"Delenie nulou")
    def test_divide6(self):
        self.assertEqual(divide(-2,-2), 1, "Ma byt 1")
    def test_divide7(self):
        self.assertEqual(divide(2,0.5), 4, "Ma byt 4")

class factorialTests(unittest.TestCase):
    def test_factorial1(self):
        self.assertEqual(factorial(5), 120, "Ma byt 120")
    def test_factorial2(self):
        self.assertEqual(factorial(1), 1, "Ma byt 1")
    def test_factorial3(self):
        self.assertEqual(factorial(0), 1, "Ma byt 1")
    def test_factorial4(self):
        self.assertRaises(ValueError, factorial(2.2), "Faktorial musi byt cele kladne cislo")
    def test_factorial5(self):
        self.assertRaises(ValueError, factorial(-6), "Faktorial musi byt cele kladne cislo")

class powerTests(unittest.TestCase):
    def test_power1(self):
        self.assertEqual(power(4,3), 64, "Ma byt 64")
    def test_power2(self):
        self.assertEqual(power(-2,5), -32, "Ma byt -32")
    def test_power3(self):
        self.assertEqual(power(1,-1), 1, "Ma byt 1")
    def test_power4(self):
        self.assertEqual(power(10,0), 1, "Ma byt 1")
    def test_power5(self):
        self.assertEqual(power(10,3), 1000, "Ma byt 1000")
    def test_power6(self):
        self.assertEqual(power(-2,-2), -0.25, "Ma byt -0.25")
    def test_power7(self):
        self.assertEqual(power(10,0.5), 3.16227766, "Ma byt 3.16227766")

class square_rootTests(unittest.TestCase):
    def test_square_root1(self):
        self.assertEqual(square_root(8,3), 2, "Ma byt 2")
    def test_square_root2(self):
        self.assertEqual(square_root(-8,3), -2, "Ma byt -2")
    def test_square_root3(self):
        self.assertEqual(square_root(1,-1), 1, "Ma byt 1")
    def test_square_root4(self):
        self.assertRaises(ValueError,square_root(10,0), "N nesmie byt 0")
    def test_square_root5(self):
        self.assertEqual(square_root(256,2), 16, "Ma byt 16")
    def test_square_root6(self):
        self.assertRaises(ValueError, square_root(-4,-2), "N nesmie byt zaporne cislo")
    def test_square_root7(self):
        self.assertEqual(square_root(10,0.5), 100, "Ma byt 100")

class abs_valueTests(unittest.TestCase):
    def test_abs_value1(self):
        self.assertEqual(abs_value(4), 4, "Ma byt 4")
    def test_abs_value2(self):
        self.assertEqual(abs_value(-2), 2, "Ma byt 2")
    def test_abs_value3(self):
        self.assertEqual(abs_value(-0.25), 0.25, "Ma byt 0.25")
    def test_abs_value4(self):
        self.assertEqual(abs_value(0.5), 0.5, "Ma byt 0.5")


class addSolve_exprTests(unittest.TestCase):

    def test_solve_expr_add1(self):
        self.assertEqual(self.mathlib.solve_expr("3 + 3"), 6, "Ma byt 6")
    def test_solve_expr_add2(self):
        self.assertEqual(self.mathlib.solve_expr("-3+ 6"), 3, "Ma byt 3")
    def test_solve_expr_add3(self):
        self.assertEqual(self.mathlib.solve_expr("0 +"),ValueError, "Ma byt ValueError")
    def test_solve_expr_add4(self):
        self.assertEqual(self.mathlib.solve_expr("10+100,0"), ValueError, "Ma byt ValueError")
    def test_solve_expr_add5(self):
        self.assertEqual(self.mathlib.solve_expr("a+bc"), ValueError, "Ma byt ValueError")
    def test_solve_expr_add6(self):
        self.assertEqual(self.mathlib.solve_expr("-3+-1"), -4, "Ma byt -4")
    def test_solve_expr_add7(self):
        self.assertEqual(self.mathlib.solve_expr("0.9+ -0.3"), 0.6, "Ma byt 0.6")

class minusSolve_exprTests(unittest.TestCase):
    def test_solve_expr_minus1(self):
        self.assertEqual(self.mathlib.solve_expr("2 --- 1"), 1, "Ma byt 1")
    def test_solve_expr_minus2(self):
        self.assertEqual(self.mathlib.solve_expr("-9- 2"), -7, "Ma byt -7")
    def test_solve_expr_minus3(self):
        self.assertEqual(self.mathlib.solve_expr("1--1"), 2, "Ma byt 2")
    def test_solve_expr_minus4(self):
        self.assertEqual(self.mathlib.solve_expr("-80 -  10"), -90, "Ma byt -90")
    def test_solve_expr_minus5(self):
        self.assertEqual(self.mathlib.solve_expr("a-b"), ValueError, "Ma byt ValueError")
    def test_solve_expr_minus6(self):
        self.assertEqual(self.mathlib.solve_expr("0,006-0,005"), ValueError, "Ma byt ValueError")
    def test_minus7(self):
        self.assertEqual(self.mathlib.solve_expr("-0.7--0.8"), 0.1, "Ma byt 0.1")

class multipySolve_exprTests(unittest.TestCase):
    def test_solve_expr_multiply1(self):
        self.assertEqual(self.mathlib.solve_expr("4*3"), 12, "Ma byt 12")
    def test_solve_expr_multiply2(self):
        self.assertEqual(self.mathlib.solve_expr("-2*  5"), -10, "Ma byt -10")
    def test_solve_expr_multiply3(self):
        self.assertEqual(self.mathlib.solve_expr("1 *    -1"), -1, "Ma byt -1")
    def test_solve_expr_multiply4(self):
        self.assertEqual(self.mathlib.solve_expr("-10*-100"), 1000, "Ma byt 1000")
    def test_solve_expr_multiply5(self):
        self.assertEqual(self.mathlib.solve_expr("a*5"), ValueError, "Ma byt ValueError")
    def test_solve_expr_multiply6(self):
        self.assertEqual(self.mathlib.solve_expr("8*0.5"), 4, "Ma byt 4")
    def test_solve_expr_multiply7(self):
        self.assertEqual(self.mathlib.solve_expr("8*0,5"), ValueError, "Ma byt ValueError")

class divideSolve_exprTests(unittest.TestCase):
    def test_solve_expr_divide1(self):
        self.assertEqual(self.mathlib.solve_expr("4  /2"), 2, "Ma byt 2")
    def test_solve_expr_divide2(self):
        self.assertEqual(self.mathlib.solve_expr("-18/ 3"), -6, "Ma byt -6")
    def test_solve_expr_divide3(self):
        self.assertEqual(self.mathlib.solve_expr("a/-1"), ValueError, "Ma byt ValueError")
    def test_solve_expr_divide4(self):
        self.assertEqual(self.mathlib.solve_expr("1/10"), 0.1, "Ma byt 0.1")
    def test_solve_expr_divide5(self):
        self.assertRaises(ValueError, self.mathlib.solve_expr("5/0"),"Delenie nulou")
    def test_solve_expr_divide6(self):
        self.assertEqual(self.mathlib.solve_expr("0.5/0.5"), 1, "Ma byt 1")
    def test_solve_expr_divide7(self):
        self.assertEqual(self.mathlib.solve_expr("0,2/1"), ValueError, "Ma byt ValueError")

class factorialSolve_exprTests(unittest.TestCase):
    def test_solve_expr_factorial1(self):
        self.assertEqual(self.mathlib.solve_expr("fac5"), 120, "Ma byt 120")
    def test_solve_expr_factorial2(self):
        self.assertEqual(self.mathlib.solve_expr("fac0"), 1, "Ma byt 1")
    def test_solve_expr_factorial3(self):
        self.assertEqual(self.mathlib.solve_expr("fac1"), 1, "Ma byt 1")
    def test_solve_expr_factorial4(self):
        self.assertRaises(ValueError, self.mathlib.solve_expr("fac 5"), "Ma byt ValueError")
    def test_solve_expr_factorial5(self):
        self.assertRaises(ValueError, self.mathlib.solve_expr("fac"), "Ma byt ValueError")
    def test_solve_expr_factorial6(self):
        self.assertRaises(ValueError, self.mathlib.solve_expr("fac0.5"), "Faktorial musi byt cele kladne cislo")
    def test_solve_expr_factorial7(self):
        self.assertRaises(ValueError, self.mathlib.solve_expr("fac-2"), "Faktorial musi byt cele kladne cislo")

class powerSolve_exprTests(unittest.TestCase):
    def test_solve_expr_power1(self):
        self.assertEqual(self.mathlib.solve_expr("2^ 6"), 64, "Ma byt 64")
    def test_solve_expr_power2(self):
        self.assertEqual(self.mathlib.solve_expr("-2^5"), -32, "Ma byt -32")
    def test_solve_expr_power3(self):
        self.assertEqual(self.mathlib.solve_expr("6^0"), 1, "Ma byt 1")
    def test_solve_expr_power4(self):
        self.assertEqual(self.mathlib.solve_expr("a^2"), ValueError, "Ma byt ValueError")
    def test_solve_expr_power5(self):
        self.assertEqual(self.mathlib.solve_expr("3^"), ValueError, "Ma byt ValueError")
    def test_solve_expr_power6(self):
        self.assertEqual(self.mathlib.solve_expr("^3"), ValueError, "Ma byt ValueError")

class square_rootSolve_exprTests(unittest.TestCase):
    def test_solve_expr_square_root1(self):
        self.assertEqual(self.mathlib.solve_expr("2√4"), 2, "Ma byt 2")
    def test_solve_expr_square_root2(self):
        self.assertEqual(self.mathlib.solve_expr("3√-8"), -2, "Ma byt -2")
    def test_solve_expr_square_root3(self):
        self.assertEqual(self.mathlib.solve_expr("2√ 4"), ValueError, "Ma byt ValueError")
    def test_solve_expr_square_root4(self):
        self.assertRaises(ValueError,self.mathlib.solve_expr("0√5"), "N nesmie byt 0")
    def test_solve_expr_square_root5(self):
        self.assertEqual(self.mathlib.solve_expr("2√a"), ValueError, "Ma byt ValueError")
    def test_solve_expr_square_root6(self):
        self.assertRaises(ValueError, self.mathlib.solve_expr("-2√4"), "N nesmie byt zaporne cislo")
    def test_solve_expr_square_root7(self):
        self.assertEqual(self.mathlib.solve_expr("2√"), ValueError, "Ma byt ValueError")

class abs_valueSolve_exprTests(unittest.TestCase):
    def test_solve_expr_abs_value1(self):
        self.assertEqual(self.mathlib.solve_expr("abs4"), 4, "Ma byt 4")
    def test_solve_expr_abs_value2(self):
        self.assertEqual(self.mathlib.solve_expr("abs-2"), 2, "Ma byt 2")
    def test_solve_expr_abs_value3(self):
        self.assertEqual(self.mathlib.solve_expr("abs-0.25"), 0.25, "Ma byt 0.25")
    def test_solve_expr_abs_value4(self):
        self.assertEqual(self.mathlib.solve_expr("abs-0,25"), ValueError, "Ma byt ValueError")
    def test_solve_expr_abs_value5(self):
        self.assertEqual(self.mathlib.solve_expr("abs"), ValueError, "Ma byt ValueError")

class LongSolve_exprTests(unittest.TestCase):
    def test_solve_expr_long1(self):
        self.assertEqual(self.mathlib.solve_expr("fac5 + 4 - 4 * 4 / 4 - abs3 - abs-3.4 + 2√4 + 3√2 + 2.2^2.2 -2^-4"), 122.4641168, "Ma byt 122.4641168")
    def test_solve_expr_long2(self):
        self.assertEqual(self.mathlib.solve_expr("6√64 * 1.5 - 0.0002 / 2^3 - fac0"), 1.999975,"Ma byt 1.999975")
    def test_solve_expr_long3(self):
        self.assertEqual(self.mathlib.solve_expr("fac10 + 5 - -90 / 3 * 2^4 - 2√256 + abs-2"), 3629271, "Ma byt 3629271")
    def test_solve_expr_long4(self):
        self.assertEqual(self.mathlib.solve_expr("6√64 * 1.5 - 0.0002 / 2^3 - fac"), ValueError, "Ma byt ValueError")
    def test_solve_expr_long5(self):
        self.assertEqual(self.mathlib.solve_expr("fac10 + 5 - -90 / 3 * 2^abs - 2√256 + abs-2"), ValueError, "Ma byt ValueError")
    def test_solve_expr_long6(self):
        self.assertEqual(self.mathlib.solve_expr("fac5 + 4 - 4 * / 4 - abs3 - abs-3.4 + 2√4 + 3√2 + 2.2^2.2 -2^-4"), ValueError, "Ma byt ValueError")
if __name__ == '__main__':
    unittest.main()