from Schrodinger import plot, form, psi, potential
import numpy as np 
from sympy import * x, y = symbols('x y')
import pytest

with open(1st derivative, "r+", encoding="utf-8") as file_fd:
  fd = file_fd.read()
  
  
with open(second x derivative2, "r+", encoding="utf-8") as file_sd:
  sd = file_sd.read()

  
def test_plot():
    ''' Tests to see if the plot function from teamB_plotfunc is plotting properly'''
    points #coming soon
    plot(points)
    assert True, "An error was encountered during plot"


def test_first_derivative():
    ''' Tests to see if the first derivative function from 1st derivative is calculating the correct derivative'''
    responses = iter([x, x*sin(y)+y*cos(x)])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    first = exec(fd)
    assert first == sin(y)-y*sin(x), "Derivative was wrong"
   
  
def test_second_derivative():
  ''' Tests to see if the second derivative function from second x derivative2 is calculating the correct derivative'''
    responses = iter([x, x*sin(y)+y*cos(x)])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    second = exec(sd)
    assert second == -y*cos(x), "Derivative was wrong"
    
    
def test_form():
  responses = iter([R])
  monkeypatch.setattr('builtins.input', lambda msg: next(responses))
  form = form(90)
  assert form == np.sin(90), "Function failed to find the correct form"
  
  
def test_potential():
  responses = iter([square_well, 5])
  monkeypatch.setattr('builtins.input', lambda msg: next(responses))
  potential = potential(2)
  assert potential == 0, "Potential function encountered an error"
  
  
