#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# @package
# Profiling je skript, ktorý počíta smerodajnú odchýlku
#
# Skript bol vytvorený za účelom vykonania profilingu. Počíta smerodajnú odchýlku, ktorá
# používa veľké množstvo funkcii z našej matematickej knižnice.
# @file profiling.py
# @date 26.4.2021

import mathlib as m
import cProfile

##
# @brief počítá smerodajnú odchýlku
# @param num zoznam čísel
# @param n počet čísel
# @return smerodajná odchylka
def stand_deviation(num, n):
    return m.solve_expr("2√(1 / ({} - 1) * ({} - {} * {}^2))".format(n, pow_sum(num), n, avg(num, n)))

##
# @brief počítá sumu druhých mocnín všetkych čísel
# @param num zoznam čísel
# @return sumu druhých mocnín všetkych čísel
def pow_sum(num):
    sum = 0
    for x in num:
        sum = m.add(sum, m.power(int(x), 2))
    return sum

##
# @brief počítá priemer zo všetkych čísel
# @param num zoznam čísel
# @param n počet čísel
# @return priemer zo všetkych čísel
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
