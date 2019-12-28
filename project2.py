# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:44:46 2018

@author: 19083812
"""

# In[]

# import required modules

import math as mt
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

# In[]

# Data import and parameterization

filename = 'project2_data.txt'
data_in = np.loadtxt(filename, skiprows = 1)   # 1st row contains column names

t = data_in[:,0]
x = data_in[:,1]
y_data = data_in[:,2]

# In[]

# Define the fitting model

def func(t, a, b):
    
    y = []
    for ind in range(len(t)):
        f = (a - b*x[ind])*(mt.exp(-1*(b-a)*t[ind]))/(b+a*x[ind])
        y.append(f)
    
    return(np.array(y))

# In[]

# Curve fitting

initial_pars = [0.1, 0.1]
bnds=([0,0], [np.inf,np.inf])

popt, pcov = sc.optimize.curve_fit(func, t, y_data, p0=initial_pars,  bounds= bnds, method = 'trf')
    
# In[]

# Visualise
plt.close('all')
plt.plot(t, y_data, 'ro', markersize = 7, label = 'data')
plt.plot(t, func(t, *popt), 'k-', lw = 2, label='fit: (a=%0.3f, b=%0.3f)' % tuple(popt))
plt.legend(loc = "lower right")


# In[]


# popt is an array of the optimized parameters a & b
# pcov is an matrix whose leading diagonal represents the variance of popt

# To obtain the standard deviation of popt, simply take square roots of the diagonal elements

perr = np.sqrt(np.diag(pcov))

#let's report the parameters a & b

print('a = ' + str(format(popt[0], '5.4f')) + " ± " + str(format(perr[0], '5.4f')))
print('b = ' + str(format(popt[1], '5.4f')) + " ± " + str(format(perr[1], '5.4f')))

# In[]

# Assuming we are interested in the coefficient of determination (r-squared)

residuals_sq = [(y_data[ind] - func(t, *popt)[ind])**2 for ind in range(len(t))]
ss_res = np.sum(residuals_sq)

ss_tot = np.sum((y_data - np.mean(y_data))**2)

r_squared = float(format(1 - (ss_res / ss_tot),'.4f'))

print('R\u00b2' + '=', r_squared)