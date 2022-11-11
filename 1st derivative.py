#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:31:09 2022

@author: anusheh
"""
import sympy as sym

class Schrodinger:
    
    def derivative (psi):
        term_to_derive_by = input('enter the term in which you would like to derive by: ')
        x = sym.Symbol(term_to_derive_by)
        first = sym.diff(function)
        return first

function = input('enter a function ')
print (Schrodinger.derivative(function))