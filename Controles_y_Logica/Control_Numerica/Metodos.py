
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import Controles_y_Logica.Logica.Numerica.Metodos_Numericos as MN
import Controles_y_Logica.Logica.Edo.Edo_Log as EDO
from Controles_y_Logica.Logica.Edo.Edo_Log import Valor_en_Y
from Controles_y_Logica.Logica.Edo.Edo_Log import crear_grafico

def Met_Euler_VS(y0,h, a,v0,vs,x_min, x_max, y_min, y_max, ax):
    # Calcular la solución analítica

    # Calcular puntos usando el método de Euler
    puntos_x_euler, puntos_y_euler = MN.Met_Euler(x_min, y0, h, x_max, EDO.ecuacion_diferencial, a, v0, vs)
    
    ax.plot(puntos_x_euler, puntos_y_euler, 'b--', label='Método de Euler', markersize=4)

    ax.set_title('Comparación entre Solución Analítica y Método de Euler', fontsize=16)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('y', fontsize=14)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.grid(True)
    ax.legend(fontsize=12)

def Euler_MejoradoVS(y0,h, a,v0,vs,x_min, x_max, y_min, y_max, ax):

    puntos_x_euler_m, puntos_y_euler_m = MN.Met_Euler_Mejorado(x_min, y0, h, x_max, EDO.ecuacion_diferencial, a, v0, vs)

    ax.plot(puntos_x_euler_m, puntos_y_euler_m, 'g--', label='Método de Euler Mejorado', markersize=2)
    ax.set_title('Comparación entre Solución Analítica y Método de Euler Mejorado', fontsize=16)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('y', fontsize=14)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.grid(True)
    ax.legend(fontsize=12)

def RK4VS(y0,h, a,v0,vs,x_min, x_max, y_min, y_max,ax):
    # Cálculo de la solución analítica

    # Solución por Runge-Kutta 4 (desde x0 hasta x_max)
    puntos_x_rk4, puntos_y_rk4 = MN.Met_Runge_Kutta4(x_min, y0, h, x_max, EDO.ecuacion_diferencial, a, v0, vs)

    # Gráfico
    
    ax.plot(puntos_x_rk4, puntos_y_rk4, 'm--', label='Método de Runge-Kutta 4', markersize=3)

    ax.set_title('Comparación entre Solución Analítica y Runge-Kutta 4', fontsize=16)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('y', fontsize=14)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.grid(True)
    ax.legend(fontsize=12)
