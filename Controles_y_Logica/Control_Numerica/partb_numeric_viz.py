"""numeric_viz.py
Visualizaciones para la parte numérica.
Importa funciones desde numeric_logic.py (rhs, simulate_euler_maruyama).
Cada función devuelve (fig, ax) y guarda la figura si se pasa `fname`.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Optional, Tuple
from numeric_logic import rhs, simulate_euler_maruyama

Path("figures").mkdir(exist_ok=True)

def plot_phase_line(mu: float, zmin: float=-3.0, zmax: float=3.0, fname: Optional[str]='figures/phase_mu.png') -> Tuple[plt.Figure, plt.Axes]:
    """Dibuja la línea de fase: z vs dz/dt usando rhs() de numeric_logic."""
    zs = np.linspace(zmin, zmax, 400)
    fvals = rhs(zs, mu)
    fig, ax = plt.subplots(figsize=(6,2.5))
    ax.axhline(0, linewidth=0.5)
    ax.plot(zs, fvals, lw=1)
    ax.set_xlabel("z"); ax.set_ylabel("dz/dt")
    ax.set_title(f"Linea de fase (mu={mu})")
    ax.grid(True)
    plt.tight_layout()
    if fname:
        plt.savefig(fname, dpi=300)
    return fig, ax

def plot_noise_simulations(mu: float, sigmas=(0.0, 0.5, 1.0), z0: float=0.2, T: float=80.0, dt: float=0.02,
                           fname: Optional[str]='figures/noise_simulations.png') -> Tuple[plt.Figure, plt.Axes]:
    """Simula y dibuja realizaciones del proceso para distintos sigma usando simulate_euler_maruyama."""
    fig, ax = plt.subplots(figsize=(8,4))
    for sigma in sigmas:
        t, z = simulate_euler_maruyama(mu, z0=z0, T=T, dt=dt, sigma=sigma)
        ax.plot(t, z, label=f'sigma={sigma}')
    ax.set_xlabel('t'); ax.set_ylabel('z(t)')
    ax.set_title(f'Simulaciones con ruido (Euler–Maruyama), μ={mu}')
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    if fname:
        plt.savefig(fname, dpi=300)
    return fig, ax

if __name__ == '__main__':
    plot_phase_line(mu=1.0)
    plot_noise_simulations(mu=1.0)

