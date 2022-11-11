from teamB_plotfunc import plot
import numpy as np 
from sympy import * x, y = symbols('x y')
import pytest

with open(1st derivative, "r+", encoding="utf-8") as file_fd:
  fd = file_fd.read()
  
  
with open(second x derivative2, "r+", encoding="utf-8") as file_sd:
  sd = file_sd.read()

  
def test_plot():
    points #coming soon
    _plot(points)
    assert True, "An error was encountered during plot"


def test_first_derivative():
    responses = iter([x, x*sin(y)+y*cos(x)])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    first = exec(fd)
    assert first == sin(y)-y*sin(x), "Derivative was wrong"
   
  
def test_second_derivative():
    responses = iter([x, x*sin(y)+y*cos(x)])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    second = exec(sd)
    assert second == -y*cos(x), "Derivative was wrong"
    
    

  
