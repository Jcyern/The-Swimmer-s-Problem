import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import Parte_A.Control_Edo.Edo as ce
import Parte_A.Logica as lg
from Parte_A.Logica.Edo.Edo_Log import ecuacion_diferencial
from Parte_A.Control_Edo.Edo import Solve_VS , Explicacion, Isoclinas_VS, Valor_en_Y_VS

def Metodos(x0, y0 ,a, v0, x_max, x_min,vs, y_min, y_max, xval, punto_ok, explicacion):
        # Estos son los rangos que se preparan para todas las funciones
        rango_x = np.arange(x_min,x_max,0.25)
        rango_y = np.arange(y_min, y_max,0.25)
        Isoclinas_VS(ecuacion_diferencial,rango_x, rango_y, a, v0, x_max,y_max, x_min, y_min, vs)
        Solve_VS(x0, y0 ,a, v0, x_max, x_min,vs, y_min, y_max, xval, punto_ok)
        if explicacion:
            C = lg.Edo.Edo_Log.solucion_diferencial(x0, y0, a, v0, vs)
            y = Valor_en_Y_VS(xval, v0, vs, a, C)
            Explicacion(punto_ok, x0,y0, a,v0,vs,xval, y, C)