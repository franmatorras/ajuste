# -*- coding: utf-8 -*-
"""
FRANCISCO MATORRAS CUEVAS

november 2019

This code works for fitting a bunch of data to a straight line, though you can
easily change it to fit any other kind of function
"""
from scipy.optimize import curve_fit as cf
import numpy as np
import matplotlib.pyplot as plt
import csv

def function(x, m, n):
    '''
    Define the kind of function you are trying to fit your data to
    Arguments:
        x, data from the horizontal axis
        m, slope from the function
        n, point where the function crosses the y axis
    Return:
        value for the equation it has been used
    '''
    return m*x + n

def fit(x, y, error):
    '''
    Fits the data you give to it to the function you have previously defined
    Arguments:
        x, data fos the x axis
        y, data for the y axis
        error, relative error for the variable in the y axis
    Return:
        popt, slope of the fit
        uncertainty for the slope
    '''
    popt, pcov = cf(function, x, y, sigma = error)
    return popt, np.sqrt(np.diag(pcov))

def main():
    '''
    Grabs the data from the file it is told and plots it with its fit and error 
    bars
    '''
    #data = numpy.genfromtxt('practica_entalpia.txt', delimiter= '\t', skip_header=2)
        
    #arrays to be used for storing info are created
    lnp = np.array([])
    t = np.array([])
    er = np.array([])
    p = np.array([])
    
    #data is taken from the text file and introduced into the arrays
    with open('practica_entalpia.txt') as data:
        filereader = csv.reader(data, delimiter ='\t')
        for row in filereader:
            lnp = np.append(lnp, float(row[0]))
            er = np.append(er, float(row[1]))
            t = np.append(t, float(row[2]))
    with open('presion.txt') as data:
        filereader = csv.reader(data, delimiter ='\t')
        for row in filereader:
            p = np.append(p, float(row[0]))            
            
    #new array is made with two column, one for each axis
    data = np.array([t, lnp])
    
    #uncertainty array is created and filled
    eln = np.array([])
    eln = er/p
    
    #fit is calculated and stored in the variables 'ajuste' and 'error'
    ajuste, error = fit(t, lnp, eln)
    print('ajuste: ', ajuste)
    #the fit and error bars are plot
    #Hplt.plot(data[0,],data[1,], 'o', 'red')
    
    plt.errorbar(t, lnp, eln, fmt = 'o', ecolor = 'blue', color = 'red', barsabove = True)
    
    
    #limits are set, so that the focus is in the point it is wanted
    x = np.linspace(0.0028,0.0034,2)
    y = function(x, ajuste[0], ajuste[1])
    plt.plot(x,y, color = 'green')
    plt.grid()
    plt.ylim(2,5)
    plt.xlim(0.0028,0.0034)
    plt.show()
main()