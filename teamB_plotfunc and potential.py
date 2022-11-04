"""
Created on Fri Nov  4 12:37:23 2022

@author: anusheh
"""
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

        print ('For the potentials there are a few built in options: 1D_SHO, 0_potential, square_well, potential_step or you can choose to enter a custom potential')
        v_x_selected = input('enter potential V(x): ')
        if v_x_selected == '1D_SHO':
            k= int(input('What is your spring constant k: '))
            v_x = 0.5*k*x
        elif v_x_selected == '0_potential':
            v_x = 0
        elif v_x_selected == 'square_well':
            a = int(input('enter the size of your well: '))
            if x <= a or x <= -1*a:
                v_x = 0
            else:
                v_x = np.inf
        elif v_x_selected == 'potential_step':
            v_0 = input('enter the v(x) value at the potential step: ')
            b = input('enter x value in which the potential steps: ')
            if  b < x:
                v_x = v_0
            else:
                v_x = 0
        else:
            v_x = input('enter your custom potential equation: ')
        return v_x


    def plot(x, v_x, psi):
    '''
            function to plot the wave function as a function of x 
            this function takes in (x, v_x, psi) where:
            x is the x data
            v_x is the potential
            psi is the wavefunction
            
            for the colour choices of lines in this graph we use the standard colour options within matplotlib
            the colour options listed are as follows : red [r], blue [b], green [g], cyan [c], magenta [m], black [k]
            however more are available for the full list look up matplotlib.pyplot colour options.
            
            within this function there is also the possibility to plot the potential V(x) against x on the same graph 
            to do this reply [y] to the input of (would you like to plot potential?)
    '''
            
            
            own_colour = input ('would you like custom colour? [y] or [n]')
            fig, ax = plt.subplots()


            potential_label = input ('would you like to plot potential? [y] or [n]')
            if potential_label == 'y':
                if own_colour == 'y':
                    print ('colour options: red [r], blue [b], green [g], cyan [c], magenta [m], black [k]')
                    colour_line = input ('enter the line colour you would like for the wave function: ')
                    colour_line2 = input ('enter the line colour you would like for potential: ')
            
                else:
                    colour_line = ('k')
                    colour_line2 = ('r')
                
                ax.plot(x, np.abs(psi)**2, color=colour_line)
                ax.set_xlabel("x [arb units]")
                ax.set_ylabel("$|\Psi(x, t=0)|^2$", color=colour_line)
                ax_twin = ax.twinx()
                ax_twin.plot(x, v_x, color=colour_line2)
                ax_twin.set_ylabel("$V(x)$", color=colour_line2)    
            else:
                if own_colour == 'y':
                    print ('colour options: red [r], blue [b], green [g], cyan [c], magenta [m], black [k]')
                    colour_line = input ('enter the line colour you would like for the wave function: ')        
                else:
                    colour_line = ('k')           
            ax.plot(x, np.abs(psi)**2, color=colour_line)
            ax.set_xlabel("x")
            ax.set_ylabel("$|\Psi(x, t=0)|^2$", color=colour_line)
            
            
            
            plt.plot()

    def time_div(x, v_x, psi):
        import numpy as np
        from findiff import FinDiff, coefficients, Coefficient
        



