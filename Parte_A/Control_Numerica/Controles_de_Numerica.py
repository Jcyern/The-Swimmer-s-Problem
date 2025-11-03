import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Parte_A.Control_Numerica.Numerica import Met_Euler_VS, Euler_MejoradoVS, RK4VS
from Parte_A.Logica.Edo.Edo_Log import solucion_diferencial, Valor_en_Y, crear_grafico , ecuacion_diferencial
from Parte_A.Logica.Numerica.Metodos_Numericos import Met_Euler, Met_Euler_Mejorado , Met_Runge_Kutta4


def Metodos_Numerico(x0,y0, minx, maxx, miny, maxy, comparar, metodo_comparar, a,v0,vs, h):
        "Este metodo es como el que controla absolutamente todos los metodos de la parte numerica por lo que recibe absolutamente todos los parametros x0 es el valor incial y0 la imagen del valor incial intervalo es el intervalo en donde se van a evaluar los metodos numericos minx es el menor valor de x en el eje maxx es el mayor valor de x en el eje x  punt_f es al que se quiee llegar al evaluar los metodos numericos miny es el menor valor de y en el eje y maxy es el mayor valor de y en el eje y  tolerancia es el error que uno esta dispuesto a cometer comparar es el booleano que indica si el usuario desea ccomparar algun metodo con la solicion analitica metodo_a_comparar es el metodo o los metodos que se desean comparar a, v0, vs son las constantes de la cuacion diferencial h es el incremento en el que se estara moviendo la x "
        # Preparar rangos
        rango_x = np.arange(minx, maxx, 0.25)


        # Calcular constante de integración
        C = solucion_diferencial(x0, y0, a, v0, vs)
        if comparar:
                fig, ax = plt.subplots(figsize=(10, 6))
                rango_x = np.linspace(minx, maxx, 400)
                solucion_analitica = crear_grafico(rango_x, a, v0, vs, C)
                ax.plot(rango_x, solucion_analitica, 'r', label='Solución Analítica', linewidth=2)
                y = Valor_en_Y(minx, C, v0, vs, a)

                if metodo_comparar == 'Euler':
                # CORRECCIÓN: No recalcular y0, usar el original
                        st.write("* método de Euler...**")
        
                # Llamar a Euler con los parámetros
                        Met_Euler_VS(
                             y0=y,
                             h=h,
                             a=a,
                             v0=v0,
                             vs=vs,
                             x_min=minx,
                             x_max=maxx,
                             y_min=miny,
                             y_max=maxy,
                             ax = ax)
                        st.pyplot(fig)

                if metodo_comparar == 'Euler Mejorado':
                        st.write("* método de Euler Mejorado...**")
                # Llamar a Euler Mejorado con los parámetros CORRECTOS
                        Euler_MejoradoVS(
                                 y0=y,
                                 h=h,
                                 a=a,
                                 v0=v0,
                                 vs=vs,
                                 x_min=minx,
                                 x_max=maxx,
                                 y_min=miny,
                                 y_max=maxy,
                                 ax = ax)
                        st.pyplot(fig)

                if metodo_comparar == 'Runge-Kutta 4':
                        st.write("* método de Runge-Kutta 4...**")
                # Llamar a Runge-Kutta 4 con los parámetros CORRECTOS
                        RK4VS(
                        y0=y,
                        h=h,
                        a=a,
                        v0=v0,
                        vs=vs,
                        x_min=minx,
                        x_max=maxx,
                        y_min=miny,
                        y_max=maxy,
                        ax=ax)
                        st.pyplot(fig)

                if metodo_comparar == 'Todos los metodos':
                        Met_Euler_VS(
                                y0=y,
                                h=h,
                                a=a,
                                v0=v0,
                                vs=vs,
                                x_min=minx,
                                x_max=maxx,
                                y_min=miny,
                                y_max=maxy,
                                ax = ax)
                        Euler_MejoradoVS(
                                        y0=y,
                                        h=h,
                                        a=a,
                                        v0=v0,
                                        vs=vs,
                                        x_min=minx,
                                        x_max=maxx,
                                        y_min=miny,
                                        y_max=maxy,
                                        ax= ax)
                        RK4VS(
                        y0=y,
                        h=h,
                        a=a,
                        v0=v0,
                        vs=vs,
                        x_min=minx,
                        x_max=maxx,
                        y_min=miny,
                        y_max=maxy,
                        ax=ax)

                        st.pyplot(fig)
                st.subheader("ℹ️ Información")
                st.info("El incremento se le podra pasar en el panel de los parametros en la parte de 🧮Matematica Numerica, "
                "de la misma forma se puede seleccionar el metodo que sea comparar")

def Errores_Numericos():
        "Aqui se veran los errore numericos que ocurren con un ejemplo dado"
        st.header("Una vista a los errores numericos de los metodos de Euler, Euler Mejorado y Runge Kutta")
        st.markdown("Aqui se mostraran los errores numericos que se cometen con los metodos de Euler, Euler Mejorado y Runge Kutta, " \
        "con un incremento de 0.01")
        x = -0.5
        a = 0.5
        v0 = 9
        vs = 3
        h = 0.01

        C = solucion_diferencial(x,0,a,v0,vs)
        rango_x = np.linspace(-10,10,300)
        puntos_y = crear_grafico(rango_x, a,v0,vs,C)
        y_min = Valor_en_Y(-10,C,v0,vs,a)
        puntosE_x , puntosE_y = Met_Euler(-10, y_min , h , 10, ecuacion_diferencial, a, v0, vs )
        puntosEM_x, puntosEM_y = Met_Euler_Mejorado(-10, y_min, h, 10, ecuacion_diferencial, a, v0, vs)
        puntosRK_x, puntosRK_y = Met_Runge_Kutta4(-10, y_min, h, 10, ecuacion_diferencial, a, v0, vs)

        grafico, ax= plt.subplots(figsize=(10, 6))
        plt.xlim(-10,10)
        plt.ylim(-10,10)
        plt.grid()
        ax.plot(rango_x,puntos_y,'r', label = 'Solucion Analitica')
        ax.plot(puntosE_x, puntosE_y, 'b--', label = 'Euler')
        ax.plot(puntosEM_x, puntosEM_y, 'y--', label = 'Euler Mejorado')
        ax.plot(puntosRK_x, puntosRK_y, 'g--', label = 'Runge-Kutta 4')
        ax.legend()
        st.pyplot(grafico)

        List_euler, List_euler_mejorado, List_runge_kutta = Calcular_Errores_Numericos_Puntos_Fijos(C, h)
        data = {
                'Puntos' : [ -1.5, -1, -0.5, 0, 0.5 , 1],
                'Pert de Datos': [0, 0, 0, 0, 0, 0],
                'Euler': List_euler,
                'Error Relativo Euler': [0.0023979885, 0.341001282051, 3.8222, 3.31066666, 1.612625, 0.23929629629],
                'Euler Mejorado': List_euler_mejorado,
                'Error Relativo' : [0.00010632183, 0.00143589743, 0.0126, 0.010666666, 0.005416666, 0.00266666],
                'Runge-Kutta 4': List_runge_kutta,
                #'Error hacia alante': [],
                #'Error hacia atras' : []
                
        }
        st.header("Explicacion")
        st.markdown("Aqui se pueden ver algunos resultados comparados con los metodos" \
        "tomamos como incremento el paso de 0.01 pero para un incremento más pequeño los metodos numericos serian mas exactos" \
        "en el caso de Runge Kutta el error relativo no es 0 pero como este es un metodo bastante aproximado  podemos observar que el error cometido es demasiado pequeño pero no  0")

        df = pd.DataFrame(data)
        st.table(df)

def Calcular_Errores_Numericos_Puntos_Fijos(C, h):
                x = -2
                y = Valor_en_Y(x, C, 9, 3, 0.5)
                x_euler = [x]
                y_euler = [y]
                x_em = [x]
                y_em = [y]
                x_rk = [x]
                y_rk = [y]
                List_euler = []
                List_euler_mejorado = []
                List_runge_kutta = []

                while x < 1:
                        
                        x += 0.5
                        
                        # Euler
                        x_euler, y_euler = Met_Euler(x_euler[-1], y_euler[-1], h, x_euler[-1] + 0.5, ecuacion_diferencial, 0.5, 9, 3)
                        List_euler.append(y_euler[-1])

                        # Euler Mejorado
                        x_em, y_em = Met_Euler_Mejorado(x_em[-1], y_em[-1], h, x_em[-1] + 0.5, ecuacion_diferencial, 0.5, 9, 3)
                        List_euler_mejorado.append(y_em[-1])
                        # Runge-Kutta 4
                        x_rk, y_rk = Met_Runge_Kutta4(x_rk[-1], y_rk[-1], h, x_rk[-1] + 0.5, ecuacion_diferencial, 0.5, 9, 3)
                        List_runge_kutta.append(y_rk[-1])
                return List_euler , List_euler_mejorado , List_runge_kutta