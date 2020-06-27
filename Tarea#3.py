# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:05:32 2020

@author: Owner
"""
import csv
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sc
from scipy.stats import norm
import matplotlib.mlab as mlab
import numpy as np
from fitter import Fitter
from scipy.optimize import curve_fit
from scipy import optimize
from scipy import stats
from mpl_toolkits.mplot3d import Axes3D#grafica en 3D

'''Parte 1'''

#Se crean todos los vectores a utilizar durante las pruebas

datos=[0,0,0,0]
drows=[0,0,0,0]
x0=["x1","x2","x3","x4","x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12","x13", "x14","x15"]
y=["y0","y1","y2","y3","y4","y5", "y6", "y7", "y8", "y9", "y10", "y11", "y12","y13", "y14","y15", "y16","y17", "y18","y19", "y20", "y21", "y22","y23", "y24","y25"]
x1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, 17, 18, 19,20,21,22,23,24,25]

xss=[5,6,7,8,9,10,11,12,13,14,15]
yss=[5,6,7,8,9,10,11,12,13,14,15,16, 17, 18, 19,20,21,22,23,24,25]

rows= ["x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12","x13", "x14","x15"]
#Se leen los diferentes archivos por columnas para facilitar los calculos
col_list = ["y5", "y6", "y7", "y8", "y9", "y10", "y11", "y12","y13", "y14","y15", "y16","y17", "y18","y19", "y20", "y21", "y22","y23", "y24","y25"]
df = pd.read_csv("xy.csv", usecols=col_list)

col_list2=["x","y","p"]
df1 = pd.read_csv("xyp.csv",usecols=col_list2)

#Se hace la suma de cada columna y se agreaga a la lista datos
       
datos.append(np.sum(df["y5"]))
datos.append(np.sum(df["y6"]))
datos.append(np.sum(df["y6"]))
datos.append(np.sum(df["y7"]))
datos.append(np.sum(df["y5"]))
datos.append(np.sum(df["y9"]))
datos.append(np.sum(df["y10"]))
datos.append(np.sum(df["y11"]))
datos.append(np.sum(df["y12"]))
datos.append(np.sum(df["y13"]))
datos.append(np.sum(df["y14"]))
datos.append(np.sum(df["y15"]))
datos.append(np.sum(df["y16"]))
datos.append(np.sum(df["y17"]))
datos.append(np.sum(df["y18"]))
datos.append(np.sum(df["y19"]))
datos.append(np.sum(df["y20"]))
datos.append(np.sum(df["y21"]))
datos.append(np.sum(df["y22"]))
datos.append(np.sum(df["y23"]))
datos.append(np.sum(df["y24"]))
datos.append(np.sum(df["y25"]))


df_list = df.values.tolist()
#Se hace la suma de cada fila y se añade a las lista drows
                 
drows.append(np.sum(df_list[0]))
drows.append(np.sum(df_list[1]))
drows.append(np.sum(df_list[2]))
drows.append(np.sum(df_list[3]))
drows.append(np.sum(df_list[4]))
drows.append(np.sum(df_list[5]))
drows.append(np.sum(df_list[6]))
drows.append(np.sum(df_list[7]))
drows.append(np.sum(df_list[8]))
drows.append(np.sum(df_list[9]))
drows.append(np.sum(df_list[10]))


#Creamos la funcion Gaussiana para ver si se ajusta a los datos encontrados
def gaussi(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x-mu)**2/(2*sigma**2))

#Encontramos los parametros dados por los datos
params,_ = curve_fit(gaussi, x1, drows, p0=[0, 1])
params2,_ = curve_fit(gaussi, x2, datos, p0=[0, 1])

print("Los parametos encontrados para la distribucion de X:",params)
print("Los parametos encontrados para la distribucion de Y:",params2)
#Se grafican las distintas representacions con y sin curva de ajuste
plt.figure(1)
plt.bar(x1, drows)
plt.xlabel('Valor de X')
plt.ylabel('Densidad marginal en X')
plt.title('Distribucion en X')
#plt.plot(x1, drows)
#plt.plot(x1, gaussi(x1, params[0], params[1]))


plt.figure(2)
plt.bar(x2, datos)
plt.xlabel('Valor de Y')
plt.ylabel('Densidad marginal en Y')
plt.title('Distribucion en Y')
#plt.plot(x2, datos)
#plt.plot(x2, gaussi(x2, params2[0], params2[1]))

plt.figure(3)
plt.bar(x1, drows)
plt.xlabel('Valor de X')
plt.ylabel('Densidad marginal en X')
plt.title('Distribucion en X')
#plt.plot(x1, drows)
plt.plot(x1, gaussi(x1, params[0], params[1]))


plt.figure(4)
plt.bar(x2, datos)
plt.xlabel('Valor de Y')
plt.ylabel('Densidad marginal en Y')
plt.title('Distribucion en Y')
#plt.plot(x2, datos)
plt.plot(x2, gaussi(x2, params2[0], params2[1]))




#Parte 3

#Encontramos la correlacion y la imprimimos
correlacion=0


for i in range(0, 231):
    
    correlacion+=df1["x"][i]*df1["y"][i]*df1["p"][i]
    
print("Correlacion:", correlacion)

#Se encuentra la covarianza con los parametros econtrados previamente y se imprime

mean1=params[0]
mean2=params2[0] 

covarianza=0    

for i in range(0, 231):
    
    covarianza+=(df1["x"][i]-mean1)*(df1["y"][i]-mean2)*df1["p"][i]
    
print("Covarianza:", covarianza)

#Coeficiente de Correlacion Pearson con los parametro de sigma que ya tenemos

coefPearson= (covarianza)/(params[1]*params2[1])

print("Coeficiente de Correlacion:", coefPearson)


#Parte 4

#Graficas de los ajustes en 2D

plt.figure(5)
#plt.bar(x1, drows)
plt.xlabel('Valor de X')
plt.ylabel('Densidad marginal en X')
plt.title('Distribucion en X')
#plt.plot(x1, drows)
plt.plot(x1, gaussi(x1, params[0], params[1]))


plt.figure(6)
#plt.bar(x2, datos)
plt.xlabel('Valor de Y')
plt.ylabel('Densidad marginal en Y')
plt.title('Distribucion en Y')
#plt.plot(x2, datos)
plt.plot(x2, gaussi(x2, params2[0], params2[1]))



#Creamos la matriz de coordenadas
X, Y = np.meshgrid(xss, yss)

#Creamos la funcion conjunta

funcion= (1/(2*np.pi* 3.19804209*6.04857283))*np.exp(-(((X-10.0120696)**2)/(2*3.19804209**2) + ((Y-15.01506038)**2)/(2*6.04857283)))

plt.figure(6)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, funcion)
plt.xlabel('Valor de X')
plt.ylabel('Valor de Y')
ax.set_title('Densidad conjunta')
plt.show()






    
    

        


     