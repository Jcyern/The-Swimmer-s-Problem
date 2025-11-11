import numpy as np
# Metodo de Euler
def Met_Euler(x0, y0, h, xf, funcion, a,v0,vs):
    x = [x0]
    y = [y0]

    while x[-1] + h <= xf:
        y_next = y[-1] + h * funcion(x[-1], a, v0, vs)
        x_next = x[-1] + h
        x.append(x_next)
        y.append(y_next)

    return np.array(x), np.array(y)
        
# Metodo de Euler Mejorado
def Met_Euler_Mejorado(x0, y0, h, xf, funcion, a,v0,vs):
    x = [x0]
    y = [y0]
    x1 = x0
    y1 = y0

    while x1 <= xf:
        y1 = y1 + (h/2) * (funcion(x1, a, v0, vs) + funcion(x1 + h, a, v0, vs))
        x1 = x1 + h
        x.append(x1)
        y.append(y1)
    return np.array(x), np.array(y)

# Metodo de Runge - Kutta de orden 4
def Met_Runge_Kutta4(x0, y0, h, xf, funcion, a,v0,vs):
    x = [x0]
    y = [y0]

    while x[-1] < xf:
        xi = x[-1]
        yi = y[-1]

        # Coeficientes RK4
        k1 = funcion(xi, a, v0, vs)
        k2 = funcion(xi + h/2, a, v0, vs)
        k3 = funcion(xi + h/2, a, v0, vs)
        k4 = funcion(xi + h, a, v0, vs)

        # Nueva y
        yi_next = yi + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        xi_next = xi + h

        x.append(xi_next)
        y.append(yi_next)

    return np.array(x), np.array(y)
