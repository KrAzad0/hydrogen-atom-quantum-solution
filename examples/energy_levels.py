"""
Example: Hydrogen Atom Energy Levels

Calculates and displays energy levels for hydrogen atom states
according to the formula: E_n = -13.6 eV / n^2
"""

import sys
sys.path.insert(0, '..')

import numpy as np
import matplotlib.pyplot as plt
from src.wavefunctions import energy_eigenvalue


def calculate_energy_levels(n_max=5):
    """
    Calculate energy levels for hydrogen atom up to principal quantum number n_max.
    
    Parameters:
    -----------
    n_max : int
        Maximum principal quantum number
    
    Returns:
    --------
    n_values : array
        Principal quantum numbers
    energies : array
        Energy eigenvalues in eV (converted from atomic units)
    """
    n_values = np.arange(1, n_max + 1)
    
    # Energy in atomic units (Hartree)
    energies_au = np.array([energy_eigenvalue(n) for n in n_values])
    
    # Convert to eV (1 Hartree = 27.211 eV)
    energies_ev = energies_au * 27.211
    
    return n_values, energies_ev


def print_energy_table(n_max=5):
    """
    Print energy levels in a formatted table.
    """
    print("\n" + "="*60)
    print("HYDROGEN ATOM ENERGY LEVELS")
    print("="*60)
    print(f"{'n':<5} {'E_n (eV)':<15} {'E_n (Hartree)':<15} {'Rydberg Constant':<15}")
    print("-"*60)
    
    for n in range(1, n_max + 1):
        E_hartree = energy_eigenvalue(n)
        E_ev = E_hartree * 27.211
        E_rydberg = E_hartree * 2  # 1 Ry = 0.5 Hartree
        
        print(f"{n:<5} {E_ev:<15.4f} {E_hartree:<15.6f} {E_rydberg:<15.6f}")
    
    print("="*60)
    print("Note: Rydberg constant Ry = 13.6 eV")
    print("="*60 + "\n")


def plot_energy_levels(n_max=5):
    """
    Plot hydrogen atom energy levels.
    """
    n_values, energies = calculate_energy_levels(n_max)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot energy levels
    for i, (n, E) in enumerate(zip(n_values, energies)):
        ax.hlines(E, 0, 1, colors='blue', linewidth=2)
        ax.text(1.05, E, f'n={n}\nE={E:.2f} eV', 
                fontsize=10, va='center', fontweight='bold')
    
    # Ionization limit
    ax.axhline(0, color='red', linestyle='--', linewidth=2, label='Ionization limit')
    
    # Some transition examples
    transitions = [
        (2, 1, 'Lyman α (121.6 nm)'),
        (3, 2, 'Balmer α (656.3 nm)'),
        (4, 3, 'Paschen α (1875 nm)'),
    ]
    
    for n_upper, n_lower, label in transitions:
        if n_upper <= n_max:
            E_upper = calculate_energy_levels(n_upper)[1][-1] if n_upper == n_max else energy_eigenvalue(n_upper) * 27.211
            E_lower = energy_eigenvalue(n_lower) * 27.211
            
            E_trans = E_upper - E_lower
            
            ax.annotate('', xy=(0.5, E_lower), xytext=(0.5, E_upper),
                       arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
            ax.text(0.55, (E_upper + E_lower)/2, f'ΔE={E_trans:.2f} eV\n{label}',
                   fontsize=9, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
    
    ax.set_xlim(-0.1, 1.5)
    ax.set_ylim(-15, 2)
    ax.set_ylabel('Energy (eV)', fontsize=12, fontweight='bold')
    ax.set_xticks([])
    ax.grid(True, alpha=0.3)
    ax.set_title('Hydrogen Atom Energy Levels', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig('energy_levels.png', dpi=300, bbox_inches='tight')
    print("Energy level diagram saved as 'energy_levels.png'")
    plt.show()


def calculate_transition_energy(n_upper, n_lower):
    """
    Calculate transition energy between two levels.
    
    Parameters:
    -----------
    n_upper : int
        Upper level quantum number
    n_lower : int
        Lower level quantum number
    
    Returns:
    --------
    E_trans : float
        Transition energy in eV
    wavelength : float
        Corresponding wavelength in nm (if E_trans > 0)
    """
    if n_upper <= n_lower:
        raise ValueError("n_upper must be greater than n_lower")
    
    E_upper = energy_eigenvalue(n_upper) * 27.211
    E_lower = energy_eigenvalue(n_lower) * 27.211
    E_trans = E_upper - E_lower
    
    # E = hc/λ => λ = hc/E
    hc = 1240  # eV·nm
    wavelength = hc / E_trans
    
    return E_trans, wavelength


if __name__ == "__main__":
    # Print energy table
    print_energy_table(n_max=6)
    
    # Calculate some important transitions
    print("\nIMPORTANT SPECTRAL LINES")
    print("="*60)
    
    transitions = [
        (2, 1, "Lyman α", "Ultraviolet"),
        (3, 1, "Lyman β", "Ultraviolet"),
        (3, 2, "Balmer α (Hα)", "Red (visible)"),
        (4, 2, "Balmer β (Hβ)", "Cyan (visible)"),
        (5, 2, "Balmer γ (Hγ)", "Violet (visible)"),
        (4, 3, "Paschen α", "Infrared"),
    ]
    
    print(f"{'Transition':<12} {'E (eV)':<12} {'λ (nm)':<15} {'Region':<15}")
    print("-"*60)
    
    for n_u, n_l, name, region in transitions:
        E_trans, wavelength = calculate_transition_energy(n_u, n_l)
        print(f"{name:<12} {E_trans:<12.4f} {wavelength:<15.2f} {region:<15}")
    
    print("="*60 + "\n")
    
    # Plot
    plot_energy_levels(n_max=5)
