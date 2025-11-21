import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from Controles_y_Logica.Logica.Edo.Bifurcacion_Log import estabilidad_punto_fijo

def Bifurcacion(miu_min, miu_max_, valores_rep, x_min, x_max, y_min, y_max):
    miu = np.linspace(miu_min, miu_max_, valores_rep)
    miu_estables, x_estables, miu_inestables, x_inestables = estabilidad_punto_fijo(miu)
    
    #Grafica
    fix , ax = plt.subplots(figsize=(8,6))
    ax.plot(miu_estables, x_estables, 'g', label='Puntos Fijos Estables')
    ax.plot(miu_inestables, x_inestables, 'r--', label='Puntos Fijos Inestables')
    
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel('Parámetro μ', fontsize=12)
    ax.set_ylabel('Puntos Fijos (x*)', fontsize=12)
    ax.set_title('Diagrama de Bifurcación: ẋ = μx - x²', fontsize=14)
    plt.legend()
    plt.grid()
    st.pyplot(fix)
    columna1, columna2 = st.columns(2)
    with columna1:
        st.subheader("📊 Datos del Diagrama de Bifurcación")
        st.write(f'Rango de μ: [{miu_min}, {miu_max_}]')
        st.write(f'Número de puntos evaluados: {valores_rep}')

    with columna2:
        st.subheader("🧑🏻‍🏫 Explicación del Diagrama de Bifurcación")
        st.markdown(" En este caso los puntos de equilibrio o puntos fijos son z* = 0 y z* = μ, por lo que este ultimo depende del parametro")

