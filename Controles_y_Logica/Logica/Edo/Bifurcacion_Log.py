
def ecuacion_diferencial_bif(z,t, miu):
    return miu*z - z**2

def derivada(z, t, miu):
    return miu - 2*z

def estabilidad(punto_fijo, miu):
    dx_dt = derivada(punto_fijo, 0, miu)
    return dx_dt < 0


def estabilidad_punto_fijo(miu):
    #Puntos fijos son z = 0 y z = miu
    miu_estables = []
    x_estables = []
    miu_inestables = []
    x_inestables = []

    for miu_val in miu:
        puntos_fijos = [0, miu_val]
        for i in puntos_fijos:
            if estabilidad(i, miu_val):
                miu_estables.append(miu_val)
                x_estables.append(i)
            else:
                miu_inestables.append(miu_val)
                x_inestables.append(i)  
    return miu_estables, x_estables, miu_inestables, x_inestables, 0,0