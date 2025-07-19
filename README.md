# Structure-Entropy Synchronization at K = 1 in π-Driven Systems

This repository contains the implementation and analysis of the paper *"Structure-Entropy Synchronization at K = 1 in π-Driven Systems"* by Y.Y.N. Li (published on July 11, 2025). The project explores the role of the mathematical constant \(\pi\) as a structural equilibrium point in dynamic systems governed by structure-entropy interactions, proposing that \(K = 1\) (the ratio of logarithmic growth rates of entropy and structure) acts as a natural attractor.

## Overview

The study builds on the Exponential Law of Structural Conservation (SCI), defining \(K(t) = \frac{d \log H(t)}{d \log \Phi(t)}\), where:
- \(\Phi(t) = \pi t\) represents the structure function.
- \(H(t) = |\pi \cos(\pi t)|\) represents the entropy or perturbation function.

Key findings include:
- The main formula \(K(t) = -\frac{\pi \tan(\pi t)}{\log \pi}\).
- Numerical simulations show \(K(t)\) fluctuates but consistently returns to values near 1.
- An inverse computation method uses the \(K = 1\) condition to approximate \(\pi\) via Newton's method.

## Installation

To run the code, you need Python 3.x with the following dependencies:
- `numpy`
- `matplotlib`
- `scipy`

Install the dependencies using pip:
```bash
pip install numpy matplotlib scipy








Structure-Entropy Synchronization at K = 1 in π-Driven Systems
https://doi.org/10.5281/zenodo.15862401
