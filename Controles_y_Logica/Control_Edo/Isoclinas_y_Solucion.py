import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from Controles_y_Logica.Logica.Edo.Edo_Log import Isoclinas
from Controles_y_Logica.Logica.Edo.Edo_Log import Valor_en_Y
from Controles_y_Logica.Logica.Edo.Edo_Log import solucion_diferencial as sd
from Controles_y_Logica.Logica.Edo.Edo_Log import crear_grafico as cg

def Isoclinas_VS(Funcion, rango_x, rango_y,a, v0,xlim,ylim, x_min, y_min,vs, x_vals, curvas_sol_ok, cond_inicial):
    "Calcula las curvas solucion aproximadas al valor incial que se le pase"
    #LLamado a la Parte Logica
    X,Y,U,V = Isoclinas(Funcion, rango_x, rango_y,a,v0,vs)

    fig, ax =  plt.subplots(figsize=(8, 6))
    plt.quiver(X, Y, U, V, angles="xy",width=0.0015)
    if curvas_sol_ok and len(cond_inicial) > 0:
        for C in cond_inicial:
            Ci= sd(C[0], C[1], a, v0, vs)
            y_vals = cg(x_vals, a, v0, vs, Ci)
            ax.plot(x_vals, y_vals, label=f'Curva Solucion C={Ci:.2f}')

    #Introduccion
    st.header("Observemos primero el metodo de las Isoclinas para poder sacar una aproximacion a la curva solucion de la siguiente ecuacion diferencial")
    #Partes de la grafica 
    ax.set_xlabel('Eje x', fontsize=12)
    ax.set_ylabel('Eje y', fontsize=12)
    ax.set_title('Campo de Isoclinas', fontsize=14)
    ax.grid(True, alpha=0.3)
    plt.xlim(x_min,xlim) 
    plt.ylim(y_min,ylim) 
    plt.title('Campo de Pendientes')
    plt.legend()
    st.latex("📈 Ecuación Diferencial:  dy/dx = v0*(1 - (x^4)/a^4)/vs")
    st.pyplot(fig)
    #Esta es la informacion del metodo de las isoclinas
    st.subheader("👩🏼‍💼Explicacion del Metodo de las Isoclinas")
    st.markdown("El metodo de las isoclinas es una tecnica grafica que se utiliza para analizar la forma que toma la solucion de una ecuacion diferencial de primer orden sin necesidad de resolverla de manera explicita. Consiste " \
    "en darle valores a la derivada en diferentes puntos del plano xy y dado estas trazar segmentos pequeños que representen la pendiente en esos puntos. Al unir estos segmentos, se obtiene una aproximacion visual de las curvas solucion de la ecuacion diferencial. Este metodo es especialmente util para ecuaciones diferenciales no lineales o cuando la solucion explicita es dificil de obtener.")

def Solve_VS(x0,y0, a, v0, x_max, x_min,vs, y_min, y_max, xval, punto_ok):
    "Resuelve la ecuacion diferencial con las condiciones iniciales"
    st.header("Asi se ve la curva de la solucion analitica de nuestro problema 📊")
    # Creacion de Grafico
    solucion, ax2= plt.subplots(figsize=(8, 6))
    ax2.set_xlabel('Velocidad del nadador', fontsize=12)
    ax2.set_ylabel('Velocidad con la que fluye el agua', fontsize=12)
    ax2.set_title('Curva solucion', fontsize=14)
    plt.xlim(x_min,x_max) 
    plt.ylim(y_min,y_max)
    ax2.grid(True, alpha=0.3)

    #Llamada a la parte logica
    C = sd(x0, y0, a, v0, vs)
    x = np.linspace(x_min, x_max, int(x_max)*1000)
    curva_solucion = cg(x, a, v0, vs, C)
    ax2.plot(x, curva_solucion, 'b', label='Solucion Analitica')
    ax2.legend()
    # Encontrar el valor en y para el x dado
    if punto_ok:
        y = Valor_en_Y_VS(xval, v0, vs, a, C)
        ax2.plot(xval, y, 'ro', markersize=8, label=f'Valor en x={xval}: y={y}')
        ax2.legend()
        st.pyplot(solucion)
    else:
        ax2.legend()
        st.pyplot(solucion)
    st.header("ℹ️ Información")
    st.info("En el panel de 📚Ecuaciones Diferenciales Ordinarias se pueden cambiar los valores de la curva para observar el como se comporta en diferentes valores iniciales, asi como modificar los limites de los ejes y los parametros como la velocidad del nadador, la velocidad del rio o ancho de este.")

def Valor_en_Y_VS(x,v0, vs, a, C):
    "Calcula el valor en x de la solucion"
    y = Valor_en_Y(x, C, v0, vs, a)
    return y

def Explicacion(punto_ok, x0, y0, a, v0, vs, x, y, C):

    col1, col2 = st.columns(2)
    if punto_ok:
        with col1:
            st.subheader("📊 Datos de la solución")
            st.write(f'Condicion inicial: ({x0}, {y0})')
            st.write(f"Constante de Integracion C: {C:.4f}")
            st.write(f"Valor en x = {x:.20f}: y = {y:.20f}")

        with col2:
            st.subheader("🧑🏻‍🏫 Explicación del problema")
            st.markdown(
            f"El nadador comienza en la orilla izquierda del río en el punto ({x0}, {y0}). "
            f"La velocidad del río varía a lo largo de su ancho, siendo máxima en el centro y disminuyendo hacia las orillas. "
            f"El nadador intenta cruzar el río nadando perpendicularmente a la corriente. "
            f"La velocidad del nadador (vs) es de {vs} mi/h, mientras que la velocidad del río en el centro (v0) es de {v0} mi/h. "
            f"El ancho del río (a) es de {a} mi. "
            f"La ecuación diferencial modela la trayectoria del nadador considerando la influencia de la corriente del río en su movimiento. "
            f"El río lo arrastra {y:.16f} mi abajo."
            )
    else:
        with col1:
            st.subheader("📊 Datos de la solución")
            st.write(f"Constante de Integracion C: {C:.16f}")
            st.write(f'Condicion inicial: ({x0}, {y0})')
        with col2:
            st.subheader("🧑🏻‍🏫 Explicación del problema")
            st.markdown(
            f"El nadador comienza en la orilla izquierda del río en el punto ({x0}, {y0}). "
            f"La velocidad del río varía a lo largo de su ancho, siendo máxima en el centro y disminuyendo hacia las orillas. "
            f"El nadador intenta cruzar el río nadando perpendicularmente a la corriente. "
            f"La velocidad del nadador (vs) es de {vs} mi/h, mientras que la velocidad del río en el centro (v0) es de {v0} mi/h. "
            f"El ancho del río (a) es de {a} mi. "
            f"La ecuación diferencial modela la trayectoria del nadador considerando la influencia de la corriente del río en su movimiento."
            )