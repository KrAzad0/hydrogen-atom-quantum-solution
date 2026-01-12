"""
Unit tests for hydrogen atom wavefunctions.
"""

import pytest
import numpy as np
from src.wavefunctions import (
    hydrogen_radial,
    energy_eigenvalue,
    normalization_check,
    expectation_value_r,
    probability_density_radial,
)


class TestEnergyEigenvalues:
    """
    Test energy eigenvalue calculations.
    """
    
    def test_ground_state_energy(self):
        """Test ground state energy E_1 = -0.5 Hartree."""
        E = energy_eigenvalue(1)
        assert np.isclose(E, -0.5), f"Expected -0.5 Hartree, got {E}"
    
    def test_energy_scaling(self):
        """Test energy scales as -1/(2n^2)."""
        for n in range(1, 6):
            E = energy_eigenvalue(n)
            expected = -1.0 / (2 * n**2)
            assert np.isclose(E, expected), f"Energy scaling failed for n={n}"
    
    def test_energy_monotonic(self):
        """Test that energy increases with n."""
        energies = [energy_eigenvalue(n) for n in range(1, 6)]
        for i in range(len(energies) - 1):
            assert energies[i] < energies[i+1], "Energies not monotonically increasing"
    
    def test_invalid_quantum_numbers(self):
        """Test error handling for invalid quantum numbers."""
        with pytest.raises(ValueError):
            energy_eigenvalue(0)
        
        with pytest.raises(ValueError):
            energy_eigenvalue(-1)


class TestRadialWavefunction:
    """
    Test radial wavefunction calculations.
    """
    
    def test_ground_state_shape(self):
        """Test ground state (1s) wavefunction behavior."""
        r = np.linspace(0.1, 10, 100)
        R = hydrogen_radial(r, n=1, l=0)
        
        # Should be monotonically decreasing
        dR = np.diff(R)
        assert np.all(dR <= 0), "1s orbital should be monotonically decreasing"
    
    def test_normalization_1s(self):
        """Test normalization of 1s orbital."""
        norm = normalization_check(n=1, l=0)
        assert np.isclose(norm, 1.0, atol=1e-2), f"1s normalization: expected 1.0, got {norm}"
    
    def test_normalization_2s(self):
        """Test normalization of 2s orbital."""
        norm = normalization_check(n=2, l=0)
        assert np.isclose(norm, 1.0, atol=1e-2), f"2s normalization: expected 1.0, got {norm}"
    
    def test_invalid_quantum_numbers(self):
        """Test error handling for invalid quantum numbers."""
        r = np.linspace(0.1, 10, 100)
        
        with pytest.raises(ValueError):
            hydrogen_radial(r, n=0, l=0)
        
        with pytest.raises(ValueError):
            hydrogen_radial(r, n=2, l=2)  # l must be < n
        
        with pytest.raises(ValueError):
            hydrogen_radial(r, n=1, l=-1)  # l must be >= 0


class TestExpectationValues:
    """
    Test expectation value calculations.
    """
    
    def test_expectation_r_ground_state(self):
        """Test <r> for ground state."""
        # For n=1, l=0: <r> = 1.5 * a_0
        r_exp = expectation_value_r(n=1, l=0)
        assert np.isclose(r_exp, 1.5), f"Expected 1.5, got {r_exp}"
    
    def test_expectation_r_2s_2p(self):
        """Test <r> for 2s and 2p states."""
        r_2s = expectation_value_r(n=2, l=0)
        r_2p = expectation_value_r(n=2, l=1)
        
        # Both should be positive
        assert r_2s > 0, "<r> should be positive"
        assert r_2p > 0, "<r> should be positive"
        
        # 2s should be farther from nucleus than 2p
        assert r_2s > r_2p, "<r> for 2s should be > <r> for 2p"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
