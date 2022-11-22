"""
FUNCIONES 
"""

"""
Contar los elementos de un DataFrame si es que son valores repetitivos 
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def countValuesInSerie(serie, dataInSerie):
    """
    # Description 
        * Contar los elementos de una Serie de pandas si es que son valores repetitivos

    # Parameters
        * serie : dataFrame Object - Toma un dataFrame por parametro  
        * dataInColumn : string - El dato interado

    # Returns
        * la cantidad de iteraciones de un dato 
    """
    return serie[serie == dataInSerie].size

def serieFromColumn(df,column):
    """
    # Description 
        * devuelve una seríe de elementos de un dataFrame, tomando su columna

    # Parameters
        * df : dataFrame Object - Toma un dataFrame por parametro
        * column : string - La columna del dataFrame

    # Returns
        * Serie de pandas
    """
    return df[column].value_counts()

def plotScatter3D(df,x,y,z,c,elev,azim):
    
    """
    # Description 
        * plotea un grafico de scatter en 3D

    # Parameters
        * df : dataFrame Object - Toma un dataFrame por parametro
        * x : str - recibe una columna del dataFrame
        * y : str - recibe una columna del dataFrame
        * z : str - recibe una columna del dataFrame
        * c : str - color del scatter (ver: https://matplotlib.org/stable/gallery/color/named_colors.html)
        * elev : int - stores the elevation angle in the z plane.
        * azim : int - stores the azimuth angle in the x,y plane
    """

    fig = plt.figure()
    threedee = fig.add_subplot(projection='3d')

    threedee.scatter(df[x], df[y], df[z],color=c)
    threedee.set_xlabel(x)
    threedee.set_ylabel(y)
    threedee.set_zlabel(z)
    threedee.view_init(elev, azim)
    plt.show()