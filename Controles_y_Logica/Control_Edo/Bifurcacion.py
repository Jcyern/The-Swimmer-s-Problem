"""ode_viz.py
Visualizaciones para la parte de EDO.
Importa las funciones desde ode_logic.py y produce figuras.
Cada función devuelve (fig, ax) y guarda la figura si se pasa `fname`.
"""

import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
from typing import Optional, Tuple
from ode_logic import solve_ode, mu_sweep_mean

Path("figures").mkdir(exist_ok=True)

def plot_trajectory(mu: float=1.0, z0: float=0.1, T: float=80.0,
                    t_eval: Optional[np.ndarray]=None, fname: Optional[str]='figures/ode_trajectory.png') -> Tuple[plt.Figure, plt.Axes]:
    """Traza la solución determinista usando solve_ode y devuelve (fig, ax).
    Si `fname` no es None guarda la figura en disco.
    """
    if t_eval is None:
        t_eval = np.linspace(0.0, T, 2001)
    t, z = solve_ode(mu, z0=z0, t_span=(0.0, T), t_eval=t_eval)
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(t, z, label=f"mu={mu}")
    ax.set_xlabel("t"); ax.set_ylabel("z(t)")
    ax.set_title("Trayectoria temporal de z(t)")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    if fname:
        plt.savefig(fname, dpi=300)
    return fig, ax

def plot_mu_sweep(mus, z0: float=0.1, T: float=80.0, t_eval=None, fname: Optional[str]='figures/mu_sweep_mean_z.png') -> Tuple[plt.Figure, plt.Axes]:
    """Realiza un barrido en `mus` usando la función mu_sweep_mean de lógica y traza mu vs media(z).
    Devuelve (fig, ax) y guarda si `fname` se proporciona.
    """
    mus_arr, means = mu_sweep_mean(mus, z0=z0, T=T, t_eval=t_eval)
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(mus_arr, means, '-o', markersize=4)
    ax.set_xlabel(r'$\mu$'); ax.set_ylabel('media de $z$ (ventana final)')
    ax.set_title('Media estacionaria de $z$ vs $\\mu$ (barrido paramétrico)')
    ax.grid(True)
    plt.tight_layout()
    if fname:
        plt.savefig(fname, dpi=300)
    return fig, ax

if __name__ == '__main__':
    # ejemplos rápidos
    plot_trajectory(mu=1.0)
    plot_mu_sweep(np.linspace(-1.0, 2.0, 25))

