import numpy as np
import matplotlib.pyplot as plt
#ambos dx , dy son respecto al tiempo 
def Sistema_Ecuacioness(v,y):
    dydt = v
    dvdt = -3*v -4*y
    return [dvdt, dydt]


def Plano_Fase( dx , dy, range_x: tuple , range_y:tuple, margen ):
    
    x = np.linspace(range_x[0], range_x[1], margen)
    y = np.linspace(range_y[0], range_y[1], margen)
    
    #puntos de la malla 
    X,Y = np.meshgrid(x,y)

    U =np.zeros(X.shape)
    V =  np.zeros(Y.shape)
    print(U)
    #recorrer los la matriz formada por  X,Y y darle los valores en la matriz del valor del vector U,V
    for i in range(len(x)):
        for j in range (len(y)):
            dvdt_dydt = Sistema_Ecuacioness(X[i,j],Y[i,j])
            Norma = np.sqrt(dvdt_dydt[0]**2 + dvdt_dydt[1]**2)
            U[i,j]= dvdt_dydt[0]/Norma
            V[i,j]= dvdt_dydt[1]/Norma
    
    plt.quiver(X, Y, U, V, color='darkblue' , alpha = 0.8,scale = 35)    # Flechas muy grandes
    plt.scatter(X, Y, color='red', s=5, zorder=5) 
    plt.xlabel ("velocidad")
    plt.ylabel ("altura")
    plt.title("Plano de Fase")
    plt.grid(True, alpha=0.3)
    plt.show()


Plano_Fase( 4 , 4, (-20,20) , (-20,20), 30) 