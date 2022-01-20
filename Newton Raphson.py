# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:56:49 2021

@author: Vanchhit Dubey


"""
import math as m
# Defining Function
def f(x):
    return x -m.exp(-x)

# Defining derivative of function
def g(x):
    return 1 + m.exp(-x)

#  Newton Raphson Method

def newtonRaphson(x0,e,N):
    print('\n\n NEWTON RAPHSON METHOD IMPLEMENTATION')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Error')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Input Section
x0 = 0.5
e = 10**(-6)
N = 50
# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)

# Starting Newton Raphson Method
newtonRaphson(x0,e,N)