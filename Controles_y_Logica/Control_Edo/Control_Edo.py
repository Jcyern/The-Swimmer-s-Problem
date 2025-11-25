import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import Controles_y_Logica.Logica as lg
from Controles_y_Logica.Logica.Edo.Edo_Log import ecuacion_diferencial
from Controles_y_Logica.Control_Edo.Isoclinas_y_Solucion import Solve_VS , Explicacion, Isoclinas_VS, Valor_en_Y_VS
from Controles_y_Logica.Control_Edo.Bifurcacion import Bifurcacion
from Controles_y_Logica.Control_Edo.Plano_Fase_Visual import mostrar_mi_grafico

def Metodos(x0, y0 ,a, v0, x_max, x_min,vs, y_min, y_max, xval, punto_ok, explicacion,  curvas_sol_ok, cond_inicial,  miu_min, miu_max, valores_rep, x_vals, panel, edo):
        # Estos son los rangos que se preparan para todas las funciones
        rango_x = np.arange(x_min,x_max,x_vals)
        rango_y = np.arange(y_min, y_max,x_vals)
        x_vals= np.arange(x_min,x_max,x_vals/10)
        #Hay que pasarle el x_vals desde afuera
        Isoclinas_VS(ecuacion_diferencial,rango_x, rango_y, a, v0, x_max,y_max, x_min, y_min, vs, x_vals ,curvas_sol_ok, cond_inicial)
        Solve_VS(x0, y0 ,a, v0, x_max, x_min,vs, y_min, y_max, xval, punto_ok)
        if explicacion:
            C = lg.Edo.Edo_Log.solucion_diferencial(x0, y0, a, v0, vs)
            y = Valor_en_Y_VS(xval, v0, vs, a, C)
            Explicacion(punto_ok, x0,y0, a,v0,vs,xval, y, C)
        Bifurcacion(miu_min, miu_max, valores_rep, x_min, x_max, y_min, y_max)
        mostrar_mi_grafico(panel, edo)