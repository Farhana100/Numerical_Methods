# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 23:54:10 2019

@author: PC
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

np.set_printoptions(precision=2, suppress=True, formatter={'float_kind':'{:0.10f}'.format})

X = 0
Y = 0
Z = 0

#Xcolor = '#756266'
#Ycolor = '#a7b38d'
#Zcolor = '#ba4452'
Xcolor = '#ff7d00'
Ycolor = '#ff006d'
Zcolor = '#adff02'

def Trapezoidal(strt, end, x, y):
    global X
    X += 1
    plt.fill_between([x[strt], x[end]], [y[strt], y[end]], color=Xcolor, alpha=0.5, label="Trapezoidal")
    return (x[end] - x[strt])*0.5*(y[strt] + y[end])

def Onebythree(strt, end, x, y):
    global Y
    Y += 2
    plt.fill_between([x[strt], x[strt+1], x[end]], [y[strt], y[strt+1], y[end]], color=Ycolor, alpha=0.5, label="1/3 rule")
    return (x[end] - x[strt])*(y[strt] + 4*y[strt+1] + y[end])/6.0

def threebyeight(strt, end, x, y):
    global Z
    Z += 3
    plt.fill_between([x[strt], x[strt+1], x[strt+2], x[end]], [y[strt], y[strt+1], y[strt+2], y[end]], color=Zcolor, alpha=0.5, label="3/8 rule")
    return (x[end] - x[strt])*(y[strt] + 3*y[strt+1] + 3*y[strt+2] + y[end])/8.0

def combined(l, strt, end, x, y):
    if(l == 1):
        return Trapezoidal(strt, end, x, y)
    elif(l == 2):
        return Onebythree(strt, end, x, y)
    elif(l == 3):
        return threebyeight(strt, end, x, y)
    elif(l == 4):
        return Onebythree(strt, strt+2, x, y) + Onebythree(strt+2, end, x, y)
    elif(l == 5):
        return threebyeight(strt, strt+3, x, y) + Onebythree(strt+3, end, x, y)
    elif(l == 6):
        return threebyeight(strt, strt+3, x, y) + threebyeight(strt+3, end, x, y)
            
    return threebyeight(strt, strt+3, x, y) + combined(l-3, strt+3, end, x, y)


with open("input.txt", 'r') as f:
    
    N = int(f.readline().strip())
    
    x = []
    y = []
    
    for i in range(N):
        t = f.readline().strip().split()
        x.append(float(t[0]))
        y.append(float(t[1]))
        i += 1
    
    interval = [round(x[i+1] - x[i], 5) for i in range(N-1)]
    
    subcases = [[]]
    j = 0
    
    for i in range(N-2):
        subcases[j].append(interval[i])
        if (interval[i] != interval[i+1]):
            subcases.append([])
            j += 1
            
    
    subcases[j].append(interval[i])
    
    temp = 0
    I = 0
    
    for i in range(j+1):
        l = len(subcases[i])
        
        I += combined(l, temp, l+temp, x, y)
        
        temp += l 
            
    print("Trapeziod: " + str(X) + " intervals")
    print("1/3 rule: " + str(Y) + " intervals")
    print("3/8 rule: " + str(Z) + " intervals")
    print()
    print("Integral value: " + str(I))
    
    plt.plot(x, y, color='black' )
    plt.scatter(x, y, color='black', s=5)
    plt.title("Newton-Cotes Integration")
    plt.xlabel("data x")
    plt.ylabel("data y")
    Xpatch = mpatches.Patch(color=Xcolor, label='Trapezoidal', alpha=0.5)
    Ypatch = mpatches.Patch(color=Ycolor, label='1/3 rule', alpha=0.5)
    Zpatch = mpatches.Patch(color=Zcolor, label='3/8 rule', alpha=0.5)
    plt.legend(handles=[Xpatch, Ypatch, Zpatch])

    
    