from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="hydrogen-atom-quantum-solution",
    version="1.0.0",
    author="Kumar Azad",
    author_email="kumarazad9211p@gmail.com",
    description="Complete quantum mechanical solution for hydrogen atom",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KrAzad0/hydrogen-atom-quantum-solution",
    project_urls={
        "Bug Tracker": "https://github.com/KrAzad0/hydrogen-atom-quantum-solution/issues",
        "Documentation": "https://github.com/KrAzad0/hydrogen-atom-quantum-solution",
        "Source Code": "https://github.com/KrAzad0/hydrogen-atom-quantum-solution",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "pytest-cov>=2.12.0",
            "black>=21.5b0",
            "flake8>=3.9.0",
            "pylint>=2.9.0",
        ],
        "viz": [
            "mayavi>=4.7.0",
            "plotly>=5.0.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            # Add any command-line tools here
        ],
    },
    keywords="hydrogen atom quantum mechanics Schrödinger",
    zip_safe=False,
)
