import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from Controles_y_Logica.Logica.Edo.Bifurcacion_Log import estabilidad_punto_fijo

def Bifurcacion(miu_min, miu_max_, valores_rep, x_min, x_max, y_min, y_max):
    st.header("En esta parte se podra observar el Diagrama de Bifurcacion con su explicacion correspondiente")
    miu = np.linspace(miu_min, miu_max_, valores_rep)
    miu_estables, x_estables, miu_inestables, x_inestables,x_b, y_b = estabilidad_punto_fijo(miu)
    
    #Grafica
    fix , ax = plt.subplots(figsize=(8,6))
    ax.plot(miu_estables, x_estables, 'g', label='Puntos Fijos Estables')
    ax.plot(miu_inestables, x_inestables, 'r--', label='Puntos Fijos Inestables')
    ax.plot(x_b,y_b, 'ko', markersize=8, label='Punto de Bifurcación')

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
        st.subheader("🧑🏻‍🏫 Explicacion del Diagrama de Bifurcacion")
        st.write(f'Rango de μ: [{miu_min}, {miu_max_}]')
        st.write(f'Número de puntos evaluados: {valores_rep}')
        st.markdown(r"""
### Puntos de Equilibrio

Los puntos de equilibrio se obtienen resolviendo dz/dt = 0:

$$
\mu z - z^2 = z(\mu - z) = 0
$$

$$
z = 0 \quad y \quad z = \mu
$$

### Análisis de Estabilidad

La derivada es $f'(z) = \mu - 2z$. Evaluamos en los equilibrios:

**Punto $z = 0$: $f'(0) = \mu$**

- $\mu < 0$: $f'(0) < 0$ → **Estable**
- $\mu > 0$: $f'(0) > 0$ → **Inestable**

**Punto $z = \mu$: $f'(\mu) = \mu - 2\mu = -\mu$**

- $\mu < 0$: $f'(\mu) > 0$ → **Inestable**  
- $\mu > 0$: $f'(\mu) < 0$ → **Estable**
""")
    with columna2:
        st.subheader("📊 Datos del Diagrama de Bifurcación")
        st.markdown("""
## Tipo de Bifurcación: **Transcrítica**

### Características:
- **Dos ramas de puntos fijos** se intersectan en μ = 0
- **Intercambio de estabilidad** en el punto de bifurcación  
- **Ambas ramas existen** para todo μ

### Interpretación Cualitativa

El parámetro μ representa el balance entre **propulsión y resistencia**:

**μ < 0 (Régimen sin avance):**
- Punto estable: z = 0
- El sistema tiende a velocidad cero
- La resistencia domina sobre la propulsión
- Interpretación física: **"Quedarse sin avance"**

**μ > 0 (Régimen con avance):**
- Punto estable: z = μ  
- El sistema alcanza velocidad positiva
- La propulsión domina sobre la resistencia
- Interpretación física: **"Lograr avance efectivo"**
""")

