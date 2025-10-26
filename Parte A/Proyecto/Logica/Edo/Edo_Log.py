import numpy as np
import scipy as sp
from scipy.integrate import solve_ivp

def ecuacion_diferencial(x, a, v0,vs):
    "Define la ecuacion diferencial  v0 * (1 - (x**4) / (a**4))/vs"
    return v0 * (1 - (x**4) / (a**4))/vs

def solucion_diferencial(x, y,a, v0, vs):
    "Solucion analitica de la ecuacion diferencial "
    "Retorna la constante de integracion"
    C = vs*y/v0 - x + (x**5)/(5*a**4)
    return C

def  crear_grafico(x, a, v0, vs, C):
    'Devuelve el resultado de v0*(C + x - (x**5)/(5*a**4))/vs'
    return v0*(C + x - (x**5)/(5*a**4))/vs

def Isoclinas(funcion, rango_x, rango_y, a,v0,vs):
    "Calcula las curvas solucion aproximadas al valor incial que se le pase"
    X,Y = np.meshgrid(rango_x, rango_y)
    pendiente = funcion(X,a,v0,vs)
    Norma = np.sqrt(1 + pendiente**2)
    U = 1/Norma
    V = pendiente/Norma
    return X,Y,U,V

def Valor_en_Y(x, C, v0, vs, a):
    "Calcula el valor en x de la solucion"
    y = (v0/vs) * (C + x - (x**5)/(5*a**4))
    return y