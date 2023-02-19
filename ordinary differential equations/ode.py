# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:57:34 2019

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

Label = ''

def f(x, y):
    return (x + 20.*y)*m.sin(x*y)

def Eulers_Method(x_strt, x_end, y_init, h):
    X = list(np.arange(x_strt, x_end, h))
    Y = [y_init]
    
    for i in range(len(X)-1):
        k1 = f(X[i], Y[i])
        Y.append(Y[i] + k1*h)
        
    
    plt.plot(X, Y, label = 'Eulers Method ' + str(h), marker='.')
    

def secondOrderRK( x_strt, x_end, y_init, a2, h):
    
    a1 = 1 - a2
    p2 = 1/(2.*a2)
    q11 = p2
    
    X = list(np.arange(x_strt, x_end, h))
    Y = [y_init]    
    
    for i in range(len(X)-1):
        k1 = f(X[i], Y[i])
        k2 = f(X[i] + p2*h, Y[i] + q11*k1*h)
        
        fy = a1*k1 + a2*k2
        
        Y.append(Y[i] + fy*h)
        
    
    plt.plot(X, Y, label = Label, marker='.')
    
    
def fourthOrderRK( x_strt, x_end, y_init, h):
    
    X = list(np.arange(x_strt, x_end, h))
    Y = [y_init]
    
    for i in range(len(X)-1):
        k1 = f(X[i], Y[i])
        k2 = f(X[i] + 0.5*h, Y[i] + 0.5*k1*h)
        k3 = f(X[i] + 0.5*h, Y[i] + 0.5*k2*h)
        k4 = f(X[i] + h, Y[i] + k3*h)
        
        fy = (k1 + 2.*k2 + 2.*k3 + k4)/6.0
        
        Y.append(Y[i] + fy*h)
        
    
    plt.plot(X, Y, label = 'fourth Order RK ' + str(h), marker='.')
    
   
def Huens_Method ( x_strt, x_end, y_init, h):
    global Label
    Label = 'Huens Method ' + str(h)
    secondOrderRK(x_strt, x_end, y_init, 1./2, h )
    
def Midpoint_Method  ( x_strt, x_end, y_init, h):
    global Label
    Label = 'Midpoint Method' + str(h)
    secondOrderRK(x_strt, x_end, y_init, 1., h)
    
def Ralstons_Method  ( x_strt, x_end, y_init, h):
    global Label
    Label = 'Ralstons Method' + str(h)
    secondOrderRK(x_strt, x_end, y_init, 2./3, h)
    

x0 = 0.0
x = 10.0
y0 = 4.0
i = 1

for h in [0.5, 0.1, 0.05, 0.01]:
    plt.figure(i, figsize=(30,7))
    Eulers_Method(x0, x, y0, h)
    Huens_Method(x0, x, y0, h)
    Midpoint_Method(x0, x, y0, h)
    Ralstons_Method(x0, x, y0, h)
    fourthOrderRK(x0, x, y0, h)
    plt.title("Ordinary Differential Equation" )
    plt.legend(loc=10)
    #plt.savefig('all' + str(h) + ".jpg")
    i += 1


plt.show()




 
    