#!/usr/bin/python
# -*- coding: utf-8 -*-

import mathlib as m
import cProfile

def stand_deviation(num, n):
    return m.solve_expr("2√(1 / ({} - 1) * ({} - {} * {}^2))".format(n, pow_sum(num, n), n, avg(num, n)))

def pow_sum(num, n):
    sum = 0
    for x in num:
        sum = m.add(sum, m.power(int(x), 2))
    return sum

def avg(num, n):
    sum = 0
    for x in num:
        sum = m.add(sum, int(x))
    return m.divide(sum, n)
    
if __name__ == '__main__':
    my_input = ""
    my_input = input("Vlož čísla pre štandardnú odchylku (oddelené bielimi znakmi):")
    list_num = my_input.split()
    cnt_num = len(list_num)
    print("\n")

    print (stand_deviation(list_num, cnt_num))
