import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def mostrar_mi_grafico():
    st.header(" Plano de fase y Estabilidad:")
    st.markdown( """ ### Sea  el sistema lineal  de altura lateral y(t) y su velocidad v(t):""")

    st.latex(r"""
            
            \begin{cases}
            \Large
            \frac{dy}{dt} = v \\ \\
            \Large
            \Large
            \frac{dv}{dt} = -3v - 4y
            \end{cases}
            """)
        
    st.markdown(" ##### A simple vista se nota que es   un sistema autónomo")
    st.markdown(" ##### Def: Sistema Autónomo")
    st.markdown("Un sistema de EDO se llama autónomo cuando la variable independiente (usualmente el tiempo t) no aparece explícitamente en las funciones que definen el sistema.")
                
    
    st.markdown("## Analicemos sus puntos críticos ")
    st.markdown("""######  Los puntos críticos es cuando ambos valores de las derivadas son cero , lo podemos llamar también solución de equilibrio, estos son estados donde el sistema no cambia  """)
    
    
    st.latex(r"""
            \frac{dy}{dt} = v = 0 \\ 
            \frac{dv}{dt} = -3v - 4y =0 \\ \\

            """)
    st.markdown(""" ##### Sustituyendo v en -3v -4y = 0  obtenemos : y = 0 """)
    st.markdown(" ##### Luego el punto (y,v) crítico es (0,0)")
    
mostrar_mi_grafico()
