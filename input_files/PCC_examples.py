# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 17:46:36 2018

@author: Jamiu
"""

# In[]
#illustrating conditions and loops

"""
To achive this, the procedure will simply be:
    1. Create 3 empty lists
    2. Examine the first item in mylist and determine its type
    3. Append the item to the correct list
    4. Proceed to the next item and repeat steps 2 & 3.
    5. Repeat steps 2-4 till the last item in mylist
"""

mylist = ['alex', 'bus', 1, 17, 'apple', 5.25,  1.245, 5]

slist =[]; ilist = []; flist = []

for item in mylist:
    if type(item) == str:
        slist.append(item)
    elif type(item) == int:
        ilist.append(item)
    else:
        flist.append(item)
        

ilist_new = [mylist[ind] for ind in range(len(mylist)) if type(mylist[ind]) == int]


# In[]

def add_list_items():
    
    """Calculates the sum of the numbers in a list
    
    1. First check the list elements and confirm they are real numbers
    2. Dismiss any texts or complex numbers in the list
    3. Return the sum of the real numbers in the list
    
    """
    result = 0    
    for ind in range(len(mylist)):
        if type(mylist[ind]) == str or type(mylist[ind]) == complex:
            mylist.copy().remove(mylist[ind])    
        else:
            result += mylist[ind]
    return(result)

result = add_list_items()

# In[]

file = open('Mary_Lamb.txt', 'r')
file_content = file.read()
line1 = file.readline()
lines = file.readlines()


# In[]

name = 'Joe'
age = 45
status = 'married'
num_of_kids = 2

with open(name + '.txt', 'w') as f:
    f.write('My name is %s\n' %name)
    f.write('I am %d years old\n' %age)
    f.write('I am %s with %d lovely kids' %(status, num_of_kids))
    f.close()

# In[]
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x) - np.sin(x)

plt.figure(figsize=(8, 8))
plt.subplot(2,1,1)
plt.title(" Sine Function" , fontsize=15)
plt.plot(x, y1, "ro--", linewidth=1.5, markersize=7, label = "y = sin(x)")
plt.xlabel('x', fontsize=14)
plt.ylabel('sin x', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.grid(which = 'both', axis = 'both')
plt.axis([-10, 10, -1, 1])
plt.legend(loc = 'upper right', fontsize = 10)

plt.subplot(2,1,2)
plt.title(" Trig. Function" , fontsize=15)
plt.plot(x, y2, "bo--", linewidth=1.5, markersize=7, label = "y = cos(x) - sin(x)")
plt.xlabel('x', fontsize=14)
plt.ylabel('cos(x) - sin (x)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.grid(which = 'both', axis = 'both')
plt.axis([-10, 10, -1.5, 1.5])
plt.legend(loc = 'best', fontsize = 10)

plt.tight_layout()


# In[]

dataset = np.loadtxt('wells_for_numpy.txt', skiprows = 1, usecols = (1,2,3,4,5))

years = dataset[:,0]

oil_vol = dataset[:,1]

water_vol = dataset[:,2]

BHP = dataset[:,-1]

# In[]

import pandas as pd

file = open('boston_structured.txt')
lines = file.readlines()
col_names = [((lines[index]).split())[0] for index in range(7,21)]

data = pd.read_csv('boston_structured.txt', sep='\t', names = col_names, skiprows = 22, nrows = 50)

# In[]
# Writing data to Excel

writer = pd.ExcelWriter('data2excel.xlsx')

df1 = pd.DataFrame(data.CRIM[20:50:2])
df2 = pd.DataFrame(data.INDUS[20:50:2])
df3 = pd.DataFrame(data.TAX[20:50:2])
df4 = pd.DataFrame(data.LSTAT[20:50:2])

df1.to_excel(writer, sheet_name='Sheet1', index=False, header = False, startrow= 3, startcol= 1)

df2.to_excel(writer, sheet_name='Sheet1', index=False, header = False, startrow= 3, startcol= 2)

df3.to_excel(writer, sheet_name='Sheet2', index=False, header = False, startrow= 3, startcol= 1)

df4.to_excel(writer, sheet_name='Sheet2', index=False, header = False, startrow= 3, startcol= 2)

writer.save()
writer.close()



# In[]
import scipy
from scipy.stats import norm

""" Data Input & assignment"""

dataset = np.loadtxt('GCMC_Kernels.txt', skiprows = 1)
rel_pressure = dataset[:,0]
y = dataset[:,1:]
Kernel = dataset[:,1:11]


expt_data = np.loadtxt('expt_isotherm.txt')
rp = expt_data[:,0] 
iso = expt_data[:,1] 


# In[]

""" Pressure Interpolation of input kernels"""

rp = np.linspace(min(rp),max(rp), 25)
spl_fit = scipy.interpolate.UnivariateSpline(rp, iso, k = 5)
iso = spl_fit(rp)


A_interp = []
for i in range(np.shape(Kernel)[1]):
    spl1 = scipy.interpolate.UnivariateSpline(rel_pressure.T, Kernel[:,i], k = 1, s = 0.25)
    
    A_interp.append(spl1(rp))

    """
    plt.close()
    plt.figure()
    plt.plot(rp, A_interp[i], 'g', lw=3)
    plt.plot(rel_pressure, K1, 'ro')
    
    """
    
interp_kernels = np.array(A_interp)


# In[]

""" Fitting normal distribution to data"""
dataset_pw = np.loadtxt('porewidths.txt')
pw = dataset_pw[:10]

mu, std = norm.fit(pw)
