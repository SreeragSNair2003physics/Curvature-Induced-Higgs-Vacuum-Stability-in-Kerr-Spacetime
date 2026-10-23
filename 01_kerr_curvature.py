
"""
File: 01_kerr_curvature.py

Purpose:
Calculate and plot the dimensionless Kretschmann scalar for Kerr spacetime at the equatorial plane.

Method:
Use the dimensionless radius x = r/M and spin parameter a_star = a/M to evaluate the analytical Kerr expression.

Scope:
This script explores how the curvature invariant varies with radial distance at a fixed polar angle.

Limitation:
At the equator, cos(theta) = 0, so the spin-dependent terms in this invariant vanish. This plot alone therefore does not show the effect of spin on the curvature invariant.
"""







import numpy as np
import matplotlib.pyplot as plt

# Defining the spin parameter for the black hole in dimensionless form; from a*= a/M equation

a_star=0.7

# Defining radial positions in dimensionless form; from x= r/M equation

x= np.linspace(2.5, 10.0, 200)

# Kerr curvature depends on both radius and polar angle, so let's define the polar angle

theta= np.pi / 2

# Defining trigonometric values, and terms for main equation

cos_theta= np.cos(theta) 
term1= x**6
term2= -15 * a_star**2 * x**4 * cos_theta**2
term3 = 15 * a_star**4 * x**2 * cos_theta**4
term4 = -a_star**6 * cos_theta**6
term5= x**2
term6= a_star**2 * cos_theta**2

numerator = term1 + term2 + term3 + term4

denominator = (term5 + term6)**6

curvature = 48 * numerator / denominator


# Inspect numerical results as a basic sanity check; remove if unwanted

print("First curvature value:", curvature[0])
print("Last curvature value:", curvature[-1])
print("Number of curvature values:", len(curvature))



# Plotting the dimensionless Kretschmann scalar

plt.figure(figsize=(8, 5))
plt.plot(x, curvature, label=fr"$a_*={a_star}$, $\theta=\pi/2$")
plt.xlabel("Dimensionless radius, r/M")
plt.ylabel(r"Dimensionless Kretschmann scalar, $M^4K$")
plt.title("Kerr Spacetime: Equatorial Curvature")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
