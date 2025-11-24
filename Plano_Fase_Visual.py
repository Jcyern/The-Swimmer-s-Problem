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
    st.markdown(" ##### Luego el punto (y,v) crítico es (0,0)  \n \n \n")
    st.markdown("""### Analizar  el tipo y estabilidad del punto crítico (0,0):
                """)
    st.markdown("##### Es un sistema lineal , por ende lo podemos escribir en forma matricial:")
    st.latex(r"\frac{d}{dt} \begin{bmatrix} y \\ v \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -4 & -3 \end{bmatrix} \begin{bmatrix} y \\ v \end{bmatrix}")
    st.markdown(r"""
    ##### Calculamos los valores propios de $A$ resolviendo $\det(A - \lambda I)=0$:
    
    $
    \lambda^2 + 3\lambda + 4 = 0
    $

    ###### Las soluciones son:
    $
    \lambda = \frac{-3 \pm \sqrt{-7}}{2} = -\frac{3}{2} \pm i\frac{\sqrt{7}}{2}
    $
                """)

    st.markdown(r"""
    #### Valores propios:
    $
    \lambda = \frac{-3 \pm \sqrt{-7}}{2} = -\frac{3}{2} \pm i\frac{\sqrt{7}}{2}
    $
    """)

    st.markdown("""
    - **Parte real**: $\\Re(\\lambda) = -\\frac{3}{2}$ (negativa)
    - **Parte imaginaria**: $\\Im(\\lambda) = \\pm \\frac{\\sqrt{7}}{2}$ (distinta de cero)
    """)

    
    
    
mostrar_mi_grafico()
