"""
Hydrogen Atom: Complete Quantum Mechanical Solution

A comprehensive package for solving and analyzing the quantum mechanics of hydrogen atom.
"""

__version__ = "1.0.0"
__author__ = "Kumar Azad"
__email__ = "kumarazad9211p@gmail.com"
__license__ = "MIT"

from .wavefunctions import (
    hydrogen_wavefunction,
    hydrogen_radial,
    spherical_harmonic,
    probability_density_radial,
)
from .schrodinger import (
    energy_eigenvalue,
    solve_radial_schrodinger,
)
from .numerics import (
    finite_difference_solver,
    shooting_method,
)
from .visualization import (
    plot_probability_density,
    plot_radial_distribution,
    plot_energy_levels,
)
from .spectroscopy import (
    transition_frequency,
    oscillator_strength,
    selection_rules,
)

__all__ = [
    "hydrogen_wavefunction",
    "hydrogen_radial",
    "spherical_harmonic",
    "probability_density_radial",
    "energy_eigenvalue",
    "solve_radial_schrodinger",
    "finite_difference_solver",
    "shooting_method",
    "plot_probability_density",
    "plot_radial_distribution",
    "plot_energy_levels",
    "transition_frequency",
    "oscillator_strength",
    "selection_rules",
]
