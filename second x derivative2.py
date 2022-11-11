# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sympy as sym

class Schrodinger:
    
    def derivative_2 (psi):
        
        '''
        waiting for everything else to be done
        '''
        term_to_derive_by = input('enter the term in which you would like to derive by: ')
        x = sym.Symbol(term_to_derive_by)
        first = sym.diff(psi)
        second = sym.diff(first)
        return second

function = input('enter a function ')
print (Schrodinger.derivative_2(function))