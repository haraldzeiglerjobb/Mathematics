# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pylab as pyL
import math

def f(æ):
    return æ*æ*æ*æ*æ**æ/3 #Trademark Harald

x1 = []
y1 = []

ø = 1

while ø < 100:
    x1.append(ø)
    y1.append(f(ø))
    ø = ø+1
    #ø += 1
#pyL.yscale("log")
#pyL.plot(x1,y1)

x = pyL.linspace(-10,10,1000)
y = pyL.e**x
pyL.yscale("log")
pyL.plot(x,y)
pyL.grid()

"""
Oppgave: erstatt '2*x' med andre 
matematiske uttrykk, for eksempel
y=3*(x-2)**2
y=3*math.e**x
y=10**x
y=3/(2+x**2)
y=x**0.5

"""
#pyL.yscale("log")
#pyL.xscale("log")
#pyL.plot(x,y)

