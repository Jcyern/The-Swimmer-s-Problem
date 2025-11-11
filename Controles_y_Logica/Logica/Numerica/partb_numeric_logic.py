"""numeric_logic.py
Funciones lógicas para la parte numérica del proyecto.
Contiene: rhs(mu, z), simulate_euler_maruyama(...)
"""

import numpy as np
from typing import Tuple

def rhs(z, mu):
    """Funcion rhs para el modelo unidimensional usado en los diagramas de fase:
    dz/dt = mu*z - z**2
    Acepta z escalar o array y devuelve mismo shape.
    """
    return mu*z - z**2

def simulate_euler_maruyama(mu: float, z0: float=0.0, T: float=10.0, dt: float=0.01,
                            sigma: float=0.0, seed: int=None) -> Tuple[np.ndarray, np.ndarray]:
    """Simula dz = (mu*z - z^2) dt + sigma dW usando Euler–Maruyama.
    Devuelve (t_array, z_array).
    Si sigma==0 actúa como Euler explícito determinista.
    """
    if seed is not None:
        np.random.seed(seed)
    n = int(np.ceil(T / dt))
    t = np.linspace(0, T, n+1)
    z = np.empty(n+1)
    z[0] = z0
    for i in range(n):
        zi = z[i]
        drift = rhs(zi, mu)
        if sigma == 0:
            z[i+1] = zi + drift * dt
        else:
            dw = np.sqrt(dt) * np.random.randn()
            z[i+1] = zi + drift * dt + sigma * dw
    return t, z

