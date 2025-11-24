import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def sistema(t, estado):
    y, v = estado
    dydt = v
    dvdt = -3*v - 4*y
    return [dydt, dvdt]

def Plano_Fase(  range_x: tuple , range_y:tuple, margen ):
    
    x = np.linspace(range_x[0], range_x[1], margen)
    y = np.linspace(range_y[0], range_y[1], margen)
    
    #puntos de la malla 
    Y,V = np.meshgrid(x,y)
    #recorrer los la matriz formada por  X,Y y darle los valores en la matriz del valor del vector U,
    
    dy = V
    dv = -3*V - 4*Y
    
    # NORMALIZAR los vectores (todos misma longitud)
    norma_2= np.sqrt(dy**2 + dv**2)
    
    # Evitar división por cero
    norma_2 = np.where(norma_2 == 0, 1, norma_2)

    plt.streamplot(Y,V, dy,dv, density= 3)
    # #graficar puntos criticos 
    plt.plot(0,0, "m.")
    # plt.title('Vectores en cada punto')
    # plt.xlabel('Y')
    # plt.ylabel('V')
    plt.show()
    return ( (Y,V),(dy/norma_2,dv/norma_2))




Plano_Fase(  (-3,3), (-3,3),30 )

