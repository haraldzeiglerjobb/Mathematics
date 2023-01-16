# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 11:10:31 2022

@author: habea005

"""
import matplotlib.pyplot as plt
import numpy as np

x0=-5
x1=5
N = 10
dx = 0.1

def f(x):
    return x**2+5*x-9

def vekstfart(a,b):
    return (f(b)-f(a))/(b-a)

def vekstfartx(x):
    return vekstfart(x,x+dx)

x = np.linspace(x0,x1,N)
y=vekstfartx(x)

plt.scatter(x,y)