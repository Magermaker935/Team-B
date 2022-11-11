#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:49:59 2022

@author: anusheh
"""
import numpy as np
import matplotlib.pyplot as plt
class Schrodinger:
    import numpy as np
    import matplotlib.pyplot as plt
    class Schrodinger:

        def potential(x):
            '''
            function to define the potential this has some built in potentials for commonly used scenarios
            as well as having the option to enter a custom option

            function takes in (x)

            built in options include for potential:
            1D_SHO
            0_potential
            square_well
            potential_step
            '''

            print (
                'For the potentials there are a few built in options: 1D_SHO, 0_potential, square_well, potential_step or you can choose to enter a custom potential')
            v_x_selected = input('enter potential V(x): ')
            if v_x_selected == '1D_SHO':
                k = int(input('What is your spring constant k: '))
                v_x = 0.5 * k * x * x
            elif v_x_selected == '0_potential':
                v_x = 0
            elif v_x_selected == 'square_well':
                a = int(input('enter the size of your well: '))
                if x <= a or x <= -1 * a:
                    v_x = 0
                else:
                    v_x = np.inf
            elif v_x_selected == 'potential_step':
                v_0 = input('enter the v(x) value at the potential step: ')
                b = input('enter x value in which the potential steps: ')
                if b < x:
                    v_x = v_0
                else:
                    v_x = 0
            else:
                v_x = input('enter your custom potential equation: ')
            return v_x
