# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 08:52:29 2019

@author: PC
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 06:40:59 2019

@author: PC
"""

import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(precision=2, suppress=True, formatter={'float_kind':'{:0.10f}'.format})

with open("data.txt", 'r') as f:
    
    dataX = []
    dataY = []
    
    
    for line in f:
        t = line.strip().split()
        dataX.append(float(t[0]))
        dataY.append(float(t[1]))
    
    def Amatrix(x, y, dg):
        n = len(x)
        
        A = np.matrix(np.zeros([dg+1, dg+1]))
        
        for k in range(dg+1):
            for i in range(dg+1):
                for j in range(n):
                    A[k,i] += x[j]**(i+k)
        return A
    
    def Bmatrix(x, y, dg):
        B = np.matrix(np.zeros([dg+1, 1]))
        n = len(x)
        for i in range(dg+1):
            for j in range(n):
                B[i, 0] += (x[j]**i)*y[j]
                
        return B
    
    def f(x, C):
        
        n = np.shape(C)[0]
        
        y = 0
        
        for i in range(n):
            y += C[i,0]*(x**i)
            
        return y
     
        
    def curveFitting(dataX, dataY, degree):
        
        print('Values of relevant parameters for order ', degree)
        
        A = Amatrix(dataX, dataY, degree)
        B = Bmatrix(dataX, dataY, degree)
        C = np.linalg.inv(A)*B
        #print(A)
        #print(B)
        print(C)
        sortedX = dataX.copy()
        sortedX.sort()
        
        #x = np.arange(dataX[0]-1, dataX[len(dataX)-1]+1, .5)
        #y = [f(i, C) for i in x]
        y = [f(i, C) for i in sortedX]
        #print(np.matrix(x))
        #print(np.matrix(y))
        
        #plt.plot(x, y)
        plt.plot(sortedX, y, label='Order '+str(degree))
        
        #finding correlation coefficient (r)
        
        dataYbar = 0
        size = len(dataY)
        
        for i in range(size):
            dataYbar += dataY[i]
        dataYbar /= size
        
        st = sum([(i-dataYbar)**2 for i in dataY])
        #print(st)
        sr = sum([(dataY[i] - f(dataX[i], C))**2 for i in range(size)])
        #print(sr)
        
        r = (abs(st-sr)/st)**0.5
        
        print("Correlation Coefficient, r = ", end='')
        print("{0:.10f}".format(r))
        
        
        
        
    plt.scatter(dataX, dataY, s=1, color='black')
    curveFitting(dataX, dataY, 9)
    plt.legend()
    
    plt.savefig("curvefitting.jpg")
    