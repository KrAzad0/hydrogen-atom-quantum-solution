# Hydrogen Atom: Complete Quantum Mechanical Solution

A comprehensive computational implementation of the quantum mechanical treatment of the hydrogen atom, including analytical and numerical solutions to the Schrödinger equation, wavefunction visualization, energy calculations, and spectroscopic properties.

## 📋 Overview

This project provides:

- **Analytical Solutions**: Exact solutions to the radial and angular Schrödinger equation
- **Numerical Solvers**: Finite difference and shooting method implementations
- **Wavefunction Visualization**: 3D probability density plots and radial distribution functions
- **Energy Calculations**: Eigenvalues for various quantum states (n, l, m)
- **Spectroscopy**: Transition probabilities, selection rules, and emission spectra
- **Physical Properties**: Expectation values of position, momentum, and angular momentum

## 🎯 Key Features

### Quantum State Solutions
- Principal quantum number *n* = 1, 2, 3, ...
- Angular momentum quantum number *l* = 0, 1, ..., n-1
- Magnetic quantum number *m* = -l, ..., 0, ..., l
- Spin quantum number *s* = ±1/2

### Computational Methods
- Numerical integration of radial Schrödinger equation
- Finite difference schemes
- Shooting method for eigenvalue problems
- FFT-based momentum space calculations

### Visualization
- Radial probability density P(r) = r²|R(r)|²
- Angular probability distributions |Y(θ,φ)|²
- 3D probability clouds for arbitrary states
- Energy level diagrams with transitions

## 📁 Project Structure

```
hydrogen-atom-quantum-solution/
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── schrodinger.py         # Core Schrödinger solvers
│   ├── wavefunctions.py        # Analytical wavefunction definitions
│   ├── numerics.py             # Numerical integration methods
│   ├── visualization.py        # Plotting and 3D visualization
│   ├── spectroscopy.py         # Spectroscopic calculations
│   └── utilities.py            # Helper functions
├── notebooks/
│   ├── basic_solutions.ipynb   # Fundamental states (1s, 2s, 2p, etc.)
│   ├── numerical_methods.ipynb # Numerical solver demonstration
│   ├── visualization.ipynb     # Wavefunction visualization examples
│   └── spectroscopy.ipynb      # Transition and emission calculations
├── tests/
│   ├── __init__.py
│   ├── test_wavefunctions.py
│   ├── test_numerics.py
│   └── test_spectroscopy.py
└── examples/
    ├── energy_levels.py
    ├── transition_probabilities.py
    └── radial_distribution.py
```

## 🚀 Getting Started

### Installation

```bash
git clone https://github.com/KrAzad0/hydrogen-atom-quantum-solution.git
cd hydrogen-atom-quantum-solution

pip install -r requirements.txt
```

### Quick Start

```python
from src.wavefunctions import hydrogen_wavefunction
from src.visualization import plot_probability_density
import numpy as np

# Calculate hydrogen atom ground state (1s)
psi = hydrogen_wavefunction(n=1, l=0, m=0)

# Evaluate at spatial grid
r = np.linspace(0, 10, 100)  # in Bohr radii
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)

# Visualize probability density
plot_probability_density(psi, r, theta, phi)
```

### Running Examples

```bash
# Calculate energy levels and transitions
python examples/energy_levels.py

# Compute transition probabilities
python examples/transition_probabilities.py

# Plot radial distribution functions
python examples/radial_distribution.py
```

### Jupyter Notebooks

```bash
jupyter notebook notebooks/basic_solutions.ipynb
```

## 📚 Theory

### Schrödinger Equation in Atomic Units

For the hydrogen atom with a fixed nucleus (Born-Oppenheimer approximation):

**Time-independent Schrödinger equation:**
```
[-∇²/2 - 1/r] ψ(r,θ,φ) = E ψ(r,θ,φ)
```

**Spherical separation of variables:**
```
ψ(r,θ,φ) = R(r) Y_l^m(θ,φ)
```

**Radial equation:**
```
[-d²/dr² + l(l+1)/r² - 2/r] R(r) = E R(r)
```

**Exact energy eigenvalues:**
```
E_n = -1/(2n²)  (in atomic units, Hartree)
```

### Key Quantum Numbers

| Quantum Number | Symbol | Range | Physical Meaning |
|---|---|---|---|
| Principal | n | 1, 2, 3, ... | Energy shell |
| Angular momentum | l | 0, 1, ..., n-1 | Orbital shape |
| Magnetic | m | -l, ..., 0, ..., l | Spatial orientation |
| Spin | s | ±1/2 | Electron spin projection |

## 🔧 Core Modules

### `schrodinger.py`
- Radial Schrödinger equation solver
- Eigenvalue problem setup
- Normalization routines

### `wavefunctions.py`
- Laguerre polynomial expansions
- Spherical harmonics
- Analytical hydrogen solutions
- Complex amplitude calculations

### `numerics.py`
- Finite difference schemes
- Shooting method implementation
- RK45 integrators
- Matrix eigenvalue solvers

### `visualization.py`
- 2D/3D probability density plots
- Radial distribution visualization
- Energy level diagrams
- Transition diagrams with arrows

### `spectroscopy.py`
- Oscillator strengths
- Transition probabilities
- Selection rules (Δl = ±1, Δm = 0, ±1)
- Emission spectrum calculation

## 📊 Expected Outputs

- **Ground state (1s)** wavefunction: Gaussian-like exponential decay
- **2p orbital**: Dumbbell shape with angular variation
- **Transition 2p → 1s**: Lyman alpha (10.2 eV photon)
- **Energy quantization**: -13.6 eV, -3.4 eV, -1.51 eV, ... (Rydberg series)

## 📖 References

1. Griffiths, D. J. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press.
2. Landau, L. D., & Lifshitz, E. M. (1977). *Quantum Mechanics: Non-Relativistic Theory*. Pergamon Press.
3. Shankar, R. (1994). *Principles of Quantum Mechanics* (2nd ed.). Springer.
4. Arfken, G. B., Weber, H. J., & Harris, F. E. (2012). *Mathematical Methods for Physicists*.
5. Bethe, H. A., & Salpeter, E. E. (1977). *Quantum Mechanics of One- and Two-Electron Atoms*.

## 🧪 Testing

Run the test suite:

```bash
pytest tests/ -v
```

## 📈 Roadmap

- [ ] Relativistic corrections (Dirac equation treatment)
- [ ] Fine structure and spin-orbit coupling
- [ ] Hyperfine structure
- [ ] External field effects (Stark effect, Zeeman effect)
- [ ] Multi-electron atoms (perturbation theory)
- [ ] Time-dependent solutions (wave packet dynamics)
- [ ] Quantum decoherence models
- [ ] GPU acceleration for large grid calculations

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 👤 Author

**Kumar Azad** - Physics & Mathematics Research  
Email: kumarazad9211p@gmail.com  
GitHub: [@KrAzad0](https://github.com/KrAzad0)

## 🙏 Acknowledgments

- Inspired by quantum mechanics research in attosecond physics
- Built for advanced physics graduate coursework
- References from ETH Zurich, Stanford, and IISc Bangalore curricula

## 📞 Contact & Support

- 📧 Open an issue for bugs and feature requests
- 💬 Discussions tab for questions and ideas
- 🔗 Follow for updates on quantum physics projects

---

**Last Updated**: January 2026  
**Status**: Active Development  
**Python Version**: 3.8+
