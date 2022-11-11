# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:08:43 2022

@author: Anezka
"""

import numpy as np
import matplotlib.pyplot as plt
from findiff import FinDiff
from scipy.sparse.linalg import inv
from scipy.sparse import eye, diags
import matplotlib.animation as animation

class schrodinger:
    
    def form(x):
        """
        Parameters
        ----------
        x : TYPE
            A base dimension for calculation and plotting.
        v_x : TYPE
            The potential as a function of dimension x.
        Psi : TYPE
            The wavefunction to be specified.

        Returns
        -------
        TYPE
            Psi complete with/without custom options dependant on user input.
        """
        valid = 1
        
        while valid ==  1:
            form = input("Form of data to be operated on: Reccomended[R] or Custom[C]\n")
        
            if form == "R":
                valid = 2
                return np.sin(x)
                
            elif form == "C":
                valid = 2
                print("the function follows the form y = acos(x) + ibsin(x)\n")
                a=input("Please input value for a: ")
                b=input("Please input value for b: ")
                return a*np.cos(x) + b*np.sin(x)
                
            else:
                print("This is not an accepted input parameter, please enter Reccomended[R] or Custom[C]:\n")
                valid=1
    
    
    def diff2(x,v_x,Psi):
        """
        takes some psi imported from another function
        and calculates the second derivative
        """
        # Define a grid in x
        N = 100 # larger N creates a larger resolution for the fit
        x_array = np.linspace(0, 2 * np.pi, N)
    
        # Loop over the grid and calculate the second order derivative at each point
        second_order = []
    
        #lower values of h make for a plot with higher resolution
        #numerical calculation approaches exact calculation as h tends to 0
        h = 0.1
        
        for x in x_array:
            second_order_derivative = (form(x - h) - 2 * form(x) + form(x + h)) / h ** 2 # second order differential
            second_order.append(second_order_derivative)
            
        return second_order_derivative
    
    def diff1(x,v_x,Psi):
        """
        takes some psi imported from another function
        and calculates the first derivative
        """
        # Define a grid in x
        N = 100 # larger N creates a larger resolution for the fit
        x_array = np.linspace(0, 2 * np.pi, N)
    
        # Loop over the grid and calculate the second order derivative at each point
        first_order = []
    
        #lower values of h make for a plot with higher resolution
        #numerical calculation approaches exact calculation as h tends to 0
        h = 0.1
        
        for x in x_array:
            first_order_derivative = (form(x + h) - form(x)) / h # an attempt at writing the first order differential
            first_order.append(first_order_derivative)
            
        return first_order_derivative