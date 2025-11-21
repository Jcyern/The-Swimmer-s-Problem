import streamlit as st
from Controles_y_Logica.Control_Edo.Control_Edo import Metodos
from Controles_y_Logica.Control_Numerica.Controles_de_Numerica import Metodos_Numerico, Errores_Numericos

#Titulo de la pagina
st.set_page_config(page_title="Ecuaciones Diferenciales Ordinarias y Matematica Numerica", layout="wide")
#Inicio
st.title("Bienvenidos al proyecto de Ecuaciones Diferenciales Ordinarias junto con Matematica Numerica😎")

#Pestañas y panel
tab1, tab2, tab3= st.tabs(["🏠Inicio", "📚EDO", "📈Numerica"])
panel = st.sidebar

#Esto es lo que va en el inicio aun faltan cosas por terminar y ponerlo mas bonito
#Son las pestañas
with tab1 :
    st.image("Imagenes/Nadador.jpg")
    col1 , col2 = st.columns([3,2])
    
    with col1:
        st.header("Informacion")
        st.header("Tema 3: Problema del Nadador 🏊🏼‍♂️")

    with col2:
        st.header("Equipo 3 : Los Hijos de Euler")
        col2_col1 , col2_col2 = st.columns([3,2])
        with col2_col1:
            st.header("Nombre de los integrantes:")
            st.markdown("Juan Carlos Yern Espinosa")
            st.markdown("Kamila Reinoso Asín")
            st.markdown("Ana Laura Hernández")
        with col2_col2:
            st.header("Grupo: C211")

with tab2: # Ya es resolver la parte de Edo Completamente Comencemos por mi parte

    with panel: #Panel que usaremos para pasar los parametros
        st.header("⚙️Parametros")
        with st.expander("📚 Ecuaciones Diferenciales Ordinarias"):
            st.subheader("Condiciones iniciales")
            x0 = st.number_input("Valor inicial de x" , value = -0.50)
            y0 = st.number_input("Valor inicial de y", value= 0.00)
            a = st.number_input("Ancho del rio (a)", value= 0.5)
            v0 = st.number_input("Velocidad del rio en la parte central (v0)", value= 9.00)
            vs  = st.number_input("Velocidad del nadador (vs)", value= 3.00)

            st.header("Curvas Soluciones de las Isoclinas")
            curvas_sol_ok = st.checkbox("Desea ver como actuan las curvas solucion para diferentes valores iniciales")
            cond_inicial = []
            if curvas_sol_ok:
                columnas1, columnas2 = st.columns(2)
                with columnas1:
                    x1 = st.number_input("Valor inicial de x1" , value = 0, key="x1")
                    x2 = st.number_input("Valor inicial de x2" , value = -1, key="x2")
                    x3 = st.number_input("Valor inicial de x3" , value = 1, key="x3")
                with columnas2:
                    y1 = st.number_input("Valor inicial de y1", value= 0, key="y1")
                    y2 = st.number_input("Valor inicial de y2", value= -1, key="y2")
                    y3 = st.number_input("Valor inicial de y3", value= 1, key="y3")
                cond_inicial.append( (x1, y1) )
                cond_inicial.append( (x2, y2) )
                cond_inicial.append( (x3, y3)  )


            st.subheader("Rango de solución")
            x_min = st.number_input("x mínimo", value=-5.0)
            x_max = st.number_input("x máximo", value=5.0)
            y_min = st.number_input("y mínimo", value=-5.0)
            y_max = st.number_input("y máximo", value=5.0)

            #Comprueba de que se desea saber el valor de la funcion evaluada en un punto 
            punto_ok = st.checkbox("Desea saber el valor en y para un x dado?🧐")

            if punto_ok:
                xval = st.number_input("Valor de x", value=0e-14)
            else:
                xval = 0.0
            #Si desea la explicacion de la grafica 
            explicacion = st.checkbox("Explicacion de la grafica y del ejercicio")


    #Llamada a la solucion de la edo
    Metodos(x0, y0 ,a, v0, x_max, x_min,vs, y_min, y_max, xval, punto_ok, explicacion,  curvas_sol_ok, cond_inicial)


with tab3:  #Esta pestaña es para la parte de Numerica solo
    with panel:
        #Es un panel que baja se me olvido el nombre de eso 
        with st.expander("🧮Matematica Numerica"):
            #xf = st.number_input("Valor que quiere calcular")
            h = st.number_input("Incremento", min_value=1e-14, max_value= 1000.000000, step=0.01, format="%.14f", value = 0.1)

            st.subheader("🔍 Comparación con Solución Analítica")
            comparar_analitica = st.checkbox(
            "Mostrar comparación con solución analítica",
            value=False,
            help="Superpone la solución exacta para comparar precisión por defecto es el metodo de Euler"
            )

            metodo_comparar = "Euler"

            if comparar_analitica:
                metodo_comparar = st.selectbox(
                "Método a comparar:",
            ["Euler", "Runge-Kutta 4", "Euler Mejorado","Todos los metodos"],
            index=0
    )

    st.subheader("ℹ️ Información")
    st.info("Los parametros que se utilizaron en la parte de Ecuaciones Diferenciales Ordinarias siguen influyendo en esta pestaña de Numerica por lo tanto " \
    "para intentar cambiarlos podra hacerlo desde el mismo panel")
    if comparar_analitica:
        Metodos_Numerico(x0,
                         y0,
                         x_min,
                         x_max,
                         y_min,
                         y_max,
                         comparar_analitica,
                         metodo_comparar,
                         a,v0,vs,h)
    Errores_Numericos()
