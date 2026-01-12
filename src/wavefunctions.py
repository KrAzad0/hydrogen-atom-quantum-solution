"""
Hydrogen Atom Wavefunctions Module

Analytical solutions for hydrogen atom wavefunctions including:
- Radial wavefunctions R(r)
- Spherical harmonics Y_l^m(θ, φ)
- Complete wavefunctions ψ(r, θ, φ)
- Probability density distributions
"""

import numpy as np
from scipy.special import genlaguerre, sph_harm, factorial
from scipy.integrate import quad
import warnings

# Physical constants (atomic units)
BOHR_RADIUS = 1.0  # a_0 = 1 in a.u.
RYDBERG_ENERGY = 0.5  # Ry = 0.5 a.u.
FINE_STRUCTURE = 1/137.036  # α (fine structure constant)


def hydrogen_radial(r, n, l, normalized=True):
    """
    Radial wavefunction for hydrogen atom R_{n,l}(r).
    
    Parameters:
    -----------
    r : float or array
        Radial coordinate in Bohr radii
    n : int
        Principal quantum number (n >= 1)
    l : int
        Angular momentum quantum number (0 <= l < n)
    normalized : bool
        If True, return normalized wavefunction
    
    Returns:
    --------
    R : float or array
        Radial wavefunction value(s)
    """
    r = np.asarray(r, dtype=float)
    
    if n < 1 or l < 0 or l >= n:
        raise ValueError(f"Invalid quantum numbers: n={n}, l={l}")
    
    # Normalization constant
    norm = np.sqrt((2.0 / n)**3 * factorial(n - l - 1) / (2*n*factorial(n + l)))
    
    # Dimensionless variable
    rho = 2 * r / n
    
    # Laguerre polynomial: L^{2l+1}_{n-l-1}(rho)
    L = genlaguerre(n - l - 1, 2*l + 1)
    
    # Radial wavefunction
    R = norm * np.exp(-rho/2) * (rho)**l * L(rho)
    
    return R


def spherical_harmonic(theta, phi, l, m):
    """
    Spherical harmonic Y_l^m(θ, φ).
    
    Parameters:
    -----------
    theta : float or array
        Polar angle [0, π]
    phi : float or array
        Azimuthal angle [0, 2π]
    l : int
        Angular momentum quantum number
    m : int
        Magnetic quantum number (-l <= m <= l)
    
    Returns:
    --------
    Y : complex array
        Spherical harmonic value(s)
    """
    if abs(m) > l:
        raise ValueError(f"Invalid quantum numbers: l={l}, m={m}")
    
    # Using scipy implementation
    Y = sph_harm(m, l, phi, theta)
    return Y


def hydrogen_wavefunction(r, theta, phi, n, l, m, normalize=True):
    """
    Complete hydrogen atom wavefunction ψ_{n,l,m}(r, θ, φ).
    
    Parameters:
    -----------
    r : float or array
        Radial coordinate
    theta : float or array
        Polar angle
    phi : float or array
        Azimuthal angle
    n : int
        Principal quantum number
    l : int
        Angular momentum quantum number
    m : int
        Magnetic quantum number
    normalize : bool
        If True, return normalized wavefunction
    
    Returns:
    --------
    psi : complex array
        Complete wavefunction value(s)
    """
    R = hydrogen_radial(r, n, l, normalized=normalize)
    Y = spherical_harmonic(theta, phi, l, m)
    psi = R * Y
    
    return psi


def probability_density_radial(r, n, l):
    """
    Radial probability density P(r) = r² |R(r)|².
    
    Parameters:
    -----------
    r : float or array
        Radial coordinate
    n : int
        Principal quantum number
    l : int
        Angular momentum quantum number
    
    Returns:
    --------
    P : float or array
        Radial probability density
    """
    R = hydrogen_radial(r, n, l, normalized=True)
    P = r**2 * np.abs(R)**2
    
    return P


def expectation_value_r(n, l):
    """
    Expectation value <r> for hydrogen state (n, l).
    
    Formula: <r> = a_0 * n² * [3/2 - l(l+1)/(2n²)]
    """
    return BOHR_RADIUS * n**2 * (1.5 - l*(l+1)/(2*n**2))


def expectation_value_r_squared(n, l):
    """
    Expectation value <r²> for hydrogen state (n, l).
    
    Formula: <r²> = a_0² * n⁴ * [5/2 + 1 - 3l(l+1)/(2n²)]
    """
    return (BOHR_RADIUS * n)**2 * (
        n**2 * (5/2 + 1) - 3*l*(l+1)/2
    )


def uncertainty_r(n, l):
    """
    Uncertainty in position Δr for hydrogen state (n, l).
    """
    r_sq = expectation_value_r_squared(n, l)
    r = expectation_value_r(n, l)
    delta_r = np.sqrt(r_sq - r**2)
    return delta_r


def energy_eigenvalue(n):
    """
    Energy eigenvalue for hydrogen atom state n.
    
    Formula: E_n = -1/(2n²) Hartree = -13.6/n² eV
    
    Parameters:
    -----------
    n : int
        Principal quantum number
    
    Returns:
    --------
    E : float
        Energy eigenvalue in atomic units (Hartree)
    """
    if n < 1:
        raise ValueError("Principal quantum number n must be >= 1")
    return -1.0 / (2 * n**2)


def normalization_check(n, l, r_max=50, num_points=1000):
    """
    Verify normalization of radial wavefunction.
    
    Computes integral: ∫₀^∞ |R(r)|² r² dr = 1
    """
    r = np.linspace(0, r_max, num_points)
    R = hydrogen_radial(r, n, l, normalized=True)
    P = r**2 * np.abs(R)**2
    
    # Numerical integration
    from scipy.integrate import trapezoid
    integral = trapezoid(P, r)
    
    return integral


if __name__ == "__main__":
    # Example usage
    print("Hydrogen Atom Wavefunctions Module")
    print("="*50)
    
    # Ground state
    n, l, m = 1, 0, 0
    print(f"\nGround state ({n}{['s','p','d','f'][l]})")
    print(f"Energy: {energy_eigenvalue(n):.6f} Hartree")
    print(f"<r>: {expectation_value_r(n, l):.4f} Bohr")
    print(f"Normalization check: {normalization_check(n, l):.6f}")
    
    # 2p state
    n, l, m = 2, 1, 0
    print(f"\n2p state")
    print(f"Energy: {energy_eigenvalue(n):.6f} Hartree")
    print(f"<r>: {expectation_value_r(n, l):.4f} Bohr")
    print(f"Normalization check: {normalization_check(n, l):.6f}")
