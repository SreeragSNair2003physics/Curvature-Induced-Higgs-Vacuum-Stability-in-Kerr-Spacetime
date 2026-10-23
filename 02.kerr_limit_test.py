
"""
File: test_kerr_limits.py

Purpose:
Check the Schwarzschild limit of the Kerr curvature expression and compare results for different spin values.

Method:
Evaluate the dimensionless Kretschmann scalar at a fixed polar angle and compare the non-rotating result with the known Schwarzschild expression, 48/x**6.

Outputs:
Print numerical consistency checks and spin comparisons, then save a curvature-versus-radius plot.

Limitation:
These checks verify selected properties of the calculation, not every aspect of the implementation or a Higgs-vacuum model.
"""



import numpy as np
import matplotlib.pyplot as plt


# Creating array for dimensionless radius x= r/M so calculation is invariant of black hole mass in consideration
x = np.linspace(2.5, 10.0, 200)

# Defining angles
theta = np.pi / 3
cos_theta = np.cos(theta)

# Defining the rotating (Kerr) case
def kerr_curvature(x, a_star, cos_theta):
    numerator = (x**6 - 15 * a_star**2 * x**4 * cos_theta**2 + 15 * a_star**4 * x**2 * cos_theta**4 - a_star**6 * cos_theta**6)
    denominator = (x**2 + a_star**2 * cos_theta**2)**6
    return 48 * numerator / denominator


# Defining non- rotating (schwarzschild) case for comparison for sanity check
schwarzschild = 48 / x**6
nonrotating = kerr_curvature(x, 0.0, cos_theta)
rotating = kerr_curvature(x, 0.7, cos_theta)

print("Schwarzschild limit passes:",
      np.allclose(nonrotating, schwarzschild))

print("Rotation changes the result:",
      not np.allclose(rotating, schwarzschild))

# Test the equatorial limit at a fixed radius.
equatorial_cos_theta = np.cos(np.pi / 2)

equatorial_values = [
    kerr_curvature(3.0, spin, equatorial_cos_theta)
    for spin in [0.0, 0.5, 0.9]
]

print(
    "Equatorial curvature is independent of spin:",
    np.allclose(equatorial_values, equatorial_values[0])
)

print("Maximum difference for rotating case:",
      np.max(np.abs(rotating - schwarzschild)))


# Comparing several spin values at one fixed radius to see how result varies at different spin values
print("\nCurvature comparison at x = 3, theta = 60 degrees")

x_sample = 3.0

for spin in [0.0, 0.5, 0.9]:
    value = kerr_curvature(x_sample, spin, cos_theta)
    print(f"Spin a* = {spin:.1f}: M^4 K = {value:.8f}")


# Plotting radial dependence for same three spins; i.e how (M^4 * K) changes with radius for a_star= 0, 0.5, 0.9; at fixed angle of 60 degrees
for spin in [0.0, 0.5, 0.9]:
    values = kerr_curvature(x, spin, cos_theta)
    plt.plot(x, values, label=f"a* = {spin}")


# Independently check one point using the formula directly.
x_check = 3.0
spin_check = 0.5
cos_check = np.cos(np.pi / 3)

numerator_check = (
    x_check**6
    - 15 * spin_check**2 * x_check**4 * cos_check**2
    + 15 * spin_check**4 * x_check**2 * cos_check**4
    - spin_check**6 * cos_check**6
)

denominator_check = (
    x_check**2 + spin_check**2 * cos_check**2
)**6

manual_value = 48 * numerator_check / denominator_check

function_value = kerr_curvature(
    x_check, spin_check, cos_check
)

print(
    "Direct formula check passes:",
    np.isclose(manual_value, function_value)
)    


# Check numerical safety across the radial grid.
for spin in [0.0, 0.5, 0.9]:
    values = kerr_curvature(x, spin, cos_theta)

    print(
        f"Spin a* = {spin:.1f}: all values finite:",
        np.all(np.isfinite(values))
    )

    denominator = (
        x**2 + spin**2 * cos_theta**2
    )**6

    print(
        f"Spin a* = {spin:.1f}: denominator positive:",
        np.all(denominator > 0)
    )



plt.xlabel("Dimensionless radius, r/M")
plt.ylabel("Dimensionless Kretschmann scalar, M^4 K")
plt.title("Kerr Curvature at theta = 60 degrees")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("kerr_spin_comparison.png", dpi=300)
plt.show()
