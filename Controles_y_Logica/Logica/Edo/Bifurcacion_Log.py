"""ode_logic.py
Funciones lógicas para la parte de EDO.
Contiene:
- f(t, z, mu): RHS del sistema unidimensional.
- solve_ode(mu, z0, t_span, t_eval, method): wrapper sobre scipy.integrate.solve_ivp.
- mu_sweep_mean(...): barrido determinista sobre mu que devuelve medias estacionarias.
"""

import numpy as np
from scipy.integrate import solve_ivp
from typing import Tuple, Sequence

def f(t: float, z: float, mu: float) -> float:
    """RHS: dz/dt = mu*z - z**2"""
    return mu*z - z*z

def solve_ode(mu: float, z0: float=0.1, t_span: Tuple[float,float]=(0.0, 80.0),
              t_eval: Sequence[float]=None, method: str='RK45', rtol: float=1e-6, atol: float=1e-9):
    """Resuelve la EDO determinista dz/dt = f(t,z,mu) con solve_ivp.
    Devuelve (t, z) arrays.
    """
    if t_eval is None:
        t_eval = np.linspace(t_span[0], t_span[1], 4001)
    sol = solve_ivp(lambda t,y: f(t,y,mu), t_span, [z0], t_eval=t_eval, method=method, rtol=rtol, atol=atol)
    return sol.t, sol.y[0]

def mu_sweep_mean(mus, z0=0.1, T=80.0, t_eval=None, final_window=200):
    """Para cada mu en `mus` resuelve la EDO y devuelve la lista de medias
    de z en la ventana final (últimos `final_window` puntos).
    Devuelve: (mus_array, means_array)
    """
    mus = np.asarray(list(mus))
    if t_eval is None:
        t_eval = np.linspace(0.0, T, 4001)
    means = []
    n = len(t_eval)
    if isinstance(final_window, float) and 0 < final_window < 1:
        k = int(np.ceil(final_window * n))
    else:
        k = int(final_window)
    k = max(1, min(k, n))
    for mu in mus:
        t, z = solve_ode(mu, z0=z0, t_span=(t_eval[0], t_eval[-1]), t_eval=t_eval)
        mean_final = float(np.mean(z[-k:]))
        means.append(mean_final)
    return mus, np.array(means)

