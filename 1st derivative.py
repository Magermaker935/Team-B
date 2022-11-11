#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:31:09 2022

@author: anusheh
"""
import sympy as sym

class Schrodinger:
    
    def derivative (psi):
          
        '''
        function to calculate the first derivative of the wave function
            this function takes in (psi) where:
            psi is the wavefunction
        
        this function also has an input of the term in which you would like to derive by 
        '''
        term_to_derive_by = input('enter the term in which you would like to derive by: ')
        x = sym.Symbol(term_to_derive_by)
        first = sym.diff(psi)
        return first

function = input('enter a function ')
print (Schrodinger.derivative(function))