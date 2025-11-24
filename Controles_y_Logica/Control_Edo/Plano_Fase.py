import numpy as np
#Logica del Plano de Fase 

#--- sistema de ecuaciones diferenciales ---
def sistema(z):
    y, v = z
    dy = v
    dv = -3*v - 4*y
    return [dy, dv]


def plano_de_fase(y_range=(-6, 6), v_range=(-6, 6), n_points=20):
    """
    Dibuja el plano de fase del sistema dinámico.
    
    Parámetros:
    - y_range: tupla (min, max) para el eje y
    - v_range: tupla (min, max) para el eje v
    - n_points: número de divisiones de la malla
    - condiciones: lista de condiciones iniciales [[y0, v0], ...]
    """
    # Malla de puntos
    x =np.linspace(y_range[0], y_range[1], n_points)
    y =np.linspace(v_range[0], v_range[1], n_points)

    
    Y, V = np.meshgrid(x,y)
    DY, DV = sistema([Y,V])
    
    # Normalización de los vectores
    Norma_2= np.sqrt(DY**2 + DV**2)
    
    return [Y,V,DY/Norma_2, DV/Norma_2]
