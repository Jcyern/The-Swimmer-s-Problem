import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from  ..Logica.Edo.Plano_Fase import plano_de_fase,sistema,Trayectorias
from scipy.integrate import solve_ivp  # usado para saber la soluciones del sistema 
def mostrar_mi_grafico(panel, edo):
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
    
    st.markdown("**Nos damos cuenta que su tipo y estabilidad según la tabla es Espiral Convergente ' Foco Estable ")

    st.markdown("##### Veamoslo este sistema lineal en un PLANO DE FASE para ver la espiral convergiendo a (0,0)")


    #Visual para PLANO de FASE

    st.title("Plano de fase del sistema dinámico")

    # --- Parámetros en la barra lateral ---

    with panel:
        with edo:
            st.header("Parámetros del Plano de Fase")
            col_1,col_2 = st.columns(2)
            y_min = col_1.number_input("Mínimo eje y", value=-6)
            y_max = col_2.number_input("Máximo eje y", value=6)
            col_3,col_4 = st.columns(2)
            v_min = col_3.number_input("Mínimo eje v", value=-6)
            v_max = col_4.number_input("Máximo eje v", value=6)
            n_points = st.slider("Número de puntos en la malla", 10, 40, 20)
            st.write(" ")
            st.write(" ")
            st.markdown("Condiciones Iniciales")
            col1, col2= st.columns(2)
            # st.markdown("Trayectoria 1")
            t1_y = col1.number_input("Trayectoria 1:   y(t)", value=2.0)
            t1_v = col2.number_input("v(t)", value=10.0)
            col3, col4= st.columns(2)
            
            t2_y = col3.number_input("Trayectoria 2: y(t)", value=-11.0)
            t2_v = col4.number_input("v(t)", value=1.0)
            col5, col6= st.columns(2)
            t3_y = col5.number_input("Trayectoria 3: y(t)", value=0.0)
            t3_v = col6.number_input("v(t)", value=-2.0)


            st.markdown("Rango de Tiempo (t)")
            col7,col8 = st.columns(2)
            min = col7.number_input( "Min" ,value=0)
            max = col8.number_input( "Max" ,value=10)
            st.write("")
            cant = st.number_input("Cantidad de puntos", value=300)

    Y,V,DY,DV = plano_de_fase((y_min,y_max), (v_min,v_max), n_points)
    condiciones = [[t1_y,t1_v],[t2_y,t2_v],[t3_y,t3_v]]
    t_span =(min,max)
    t_eval =np.linspace(min,max,cant)

    # --- Crear el gráfico con streamplot ---
    fig, ax = plt.subplots(figsize=(6,6))
    ax.streamplot(Y, V, DY, DV, density=1.2, arrowsize=1)
    ax.set_xlabel("y")
    ax.set_ylabel("v")
    ax.set_title("Plano de fase")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.grid(True)

    # --- Trayectorias ---
    
    fig1, ax1 = plt.subplots(figsize=(6,6))
    ax1.set_title("Trayectorias dadas por el usuario en el Plano de Fase")
    ax1.set_xlabel("y")
    ax1.set_ylabel("v")
    ax1.axhline(0, color="black", linewidth=0.5)
    ax1.axvline(0, color="black", linewidth=0.5)
    y_m  = 0
    y_ma = 0
    v_m  = 0
    v_ma = 0

    
    for ci in condiciones:
        sol = solve_ivp(sistema, t_span, ci, t_eval=t_eval)
        ax1.plot(sol.y[0], sol.y[1], label=f"CI: y={ci[0]}, v={ci[1]}")
        if(sol.y[0].min()< y_m):
            y_m = sol.y[0].min()
        if(sol.y[0].max()> y_ma):
            y_ma = sol.y[0].max()

        if(sol.y[1].min()< v_m):
            v_m = sol.y[1].min()
        if(sol.y[0].max()> v_ma):
            v_ma = sol.y[1].max()

    Y1,V1,DY1,DV1 = Trayectorias((y_m,y_ma ),(v_m,  v_ma))
    ax1.quiver(Y1, V1, DY1, DV1, color="lightgray", angles="xy", scale_units="xy", scale=1)

    
    # # --- Mostrar en Streamlit ---
    st.pyplot(fig)
    st.pyplot(fig1)

