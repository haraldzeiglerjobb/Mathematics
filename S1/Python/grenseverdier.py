# -*- coding: utf-8 -*-
"""
Python-program for å beregne grenseverdier
Bruker while eller for, dette er valgfritt
"""
steg = 0.00000000001 #delta x eller noe slikt, steglengde

def f(x):
    return 3*(x**2 -4)/(x-2)
    
x=1
#Kommenter vekk følgende while-løkke for å kjøre den
"""while x < 2:
    print(f(x))
    x = x+steg
"""    
for i in range(10000):
    print(f(x))
    x = x+steg