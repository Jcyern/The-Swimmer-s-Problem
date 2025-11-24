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

    st.markdown("#### Clasificación de los puntos críticos según tipo y estabilidad:")
    st.markdown("""
            | Casos (según tr(A) y Δ)        | Raíces de la ecuación característica | Tipo de equilibrio             |
            |--------------------------------|--------------------------------------|--------------------------------|
            | (tr(A))² > 4Δ                  | Reales, distintas y negativas        | Nodo estable                   |
            |                                | Reales, distintas y positivas        | Nodo inestable                 |
            |                                | Reales, de signos opuestos           | Punto de silla (inestable)     |
            | (tr(A))² = 4Δ                  | Reales, iguales < 0                  | Nodo estable (impropio)        |
            |                                | Reales, iguales > 0                  | Nodo inestable (impropio)      |
            | (tr(A))² < 4Δ                  | Complejas, parte real < 0            | Foco estable (espiral convergente) |
            |                                | Complejas, parte real > 0            | Foco inestable (espiral divergente) |
            |                                | Complejas, parte real = 0            | Centro o vórtice (órbitas cerradas) |


""")
    st.markdown("**Leyenda:**")
    st.markdown(" tr(A) traza de la matriz A ")
    st.markdown("Δ determinante de la matriz A")
    
    st.markdown("Nos damos cuenta que su tipo y estabilidad según la tabla es Espiral Convergente ' Foco Estable ")

    st.markdown("##### Veamoslo este sistema lineal en un PLANO DE FASE para ver la espiral convergiendo a (0,0)")

    st.title("Plano de fase del sistema dinámico")

    # --- Parámetros en la barra lateral ---
    st.sidebar.header("Parámetros del plano de fase")

    y_min = st.sidebar.number_input("Mínimo eje y", value=-6)
    y_max = st.sidebar.number_input("Máximo eje y", value=6)
    v_min = st.sidebar.number_input("Mínimo eje v", value=-6)
    v_max = st.sidebar.number_input("Máximo eje v", value=6)
    n_points = st.sidebar.slider("Número de puntos en la malla", 10, 40, 20)

mostrar_mi_grafico()
