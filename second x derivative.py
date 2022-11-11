# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sympy as sym


'''
waiting for everything else to be done
'''

class Schrodinger:
    
    def derivative_2 (psi):
        term_to_derive_by = input('enter the term in which you would like to derive by: ')
        x = sym.Symbol(term_to_derive_by)
        first = sym.diff(function)
        second = sym.diff(first)
        return second

function = input('enter a function ')
print (Schrodinger.derivative_2(function))