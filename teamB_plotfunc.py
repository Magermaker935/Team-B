"""
Created on Fri Nov  4 12:37:23 2022

@author: anusheh
"""
import numpy as np
import matplotlib.pyplot as plt
class schrodinger: 
    
    def plot(x, V_x, Psi):
            '''
            function to plot the wave function as a function of x 
            this function takes in (x, V_x, Psi) where:
            x is the x data
            V_x is the potential
            Psi is the wavefunction
            
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
                
                ax.plot(x, np.abs(Psi)**2, color=colour_line)
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
            ax.plot(x, np.abs(Psi)**2, color=colour_line)
            ax.set_xlabel("x")
            ax.set_ylabel("$|\Psi(x, t=0)|^2$", color=colour_line)
            
            
            
            plt.plot()



