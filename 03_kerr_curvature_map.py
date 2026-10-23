''' This script calculates and visualizes the dimensionless curvature (M^4K) across a grid of radial distances and 
polar angles for a rapidly rotating black hole. I also included basic numerical checks and angle comparisons to better understand 
how curvature varies across the spacetime. '''


import numpy as np
import matplotlib.pyplot as plt

# Let's slightly increase the rotation to rapid mode for our black hole
a_star = 0.9

# Create a grid of dimensionless radii and polar angle
x = np.linspace(2.5, 10.0, 200)
theta = np.linspace(0, np.pi, 180)

# Convert the one-dimensional arrays into 2D coordinate grids
X, THETA = np.meshgrid(x, theta)

# The curvature expression uses cos(theta)
cos_theta = np.cos(THETA)

# Defining the Kretschmann equation
term1= x**6
term2= -15 * a_star**2 * x**4 * cos_theta**2
term3 = 15 * a_star**4 * x**2 * cos_theta**4
term4 = -a_star**6 * cos_theta**6
term5= x**2
term6= a_star**2 * cos_theta**2

numerator = term1 + term2 + term3 + term4

denominator = (term5 + term6)**6


# Calculating the dimensionless Kretschmann scalar value
curvature = 48 * numerator / denominator

# Checking that the grid produced valid values
print("Grid shape:", curvature.shape)
print("All values finite:", np.all(np.isfinite(curvature)))
print("Minimum M^4 K:", np.min(curvature))
print("Maximum M^4 K:", np.max(curvature))

equator_index = np.argmin(np.abs(theta - np.pi / 2))

print("Angle nearest the equator:", theta[equator_index])
print("Curvature at inner equator:", curvature[equator_index, 0])
print("Curvature at inner pole:", curvature[0, 0])


# Compare curvature at the same radius for three angles.
inner_radius_index = 0

for angle in [0, np.pi / 2, np.pi]:
    angle_index = np.argmin(np.abs(theta - angle))
    value = curvature[angle_index, inner_radius_index]

    print(f"Angle = {theta[angle_index]:.4f} rad, "f"M^4 K = {value:.8f}")

# Plotting curvature across radius and polar angle.
plt.figure(figsize=(10, 6))

image = plt.pcolormesh(X, THETA, curvature, shading="auto", cmap="inferno")

plt.colorbar(image, label=r"Dimensionless curvature, $M^4 K$")
plt.xlabel(r"Dimensionless radius, $r/M$")
plt.ylabel(r"Polar angle, $\theta$ (radians)")
plt.title(fr"Kerr Curvature Map ($a_*={a_star}$)")

plt.tight_layout()
plt.savefig("kerr_curvature_map.png", dpi=300)
plt.show()
