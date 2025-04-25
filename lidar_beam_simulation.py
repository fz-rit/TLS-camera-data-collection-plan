
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
beam_divergence_deg = 0.86
beam_divergence_rad = np.deg2rad(beam_divergence_deg)
zenith_angles_deg = [-0.125, 0.125]
zenith_angles_rad = np.deg2rad(zenith_angles_deg)
sample_ranges = np.arange(1, 50, 5)
POINTS_PER_DISK = 2000  # Number of points per disk
# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Colors
beam_colors = ['green', 'purple']
footprint_colors = ['blue', 'orange']

# Loop over beams
for beam_idx, angle in enumerate(zenith_angles_rad):
    # Beam direction in 3D: assume azimuth = 0, beam lies in Y-Z plane
    dz = np.sin(angle)
    dy = np.cos(angle)
    dx = 0
    direction = np.array([dx, dy, dz])
    direction /= np.linalg.norm(direction)

    for r in sample_ranges:
        # Beam center
        center = r * direction

        # Plot beam center
        ax.scatter(*center, color=beam_colors[beam_idx])

        # Beam footprint radius
        radius = (r * beam_divergence_rad) / 2

        # Create orthonormal basis for the circle plane
        if abs(direction[2]) < 0.99:
            v = np.array([0, 0, 1])
        else:
            v = np.array([0, 1, 0])
        u1 = np.cross(direction, v)
        u1 /= np.linalg.norm(u1)
        u2 = np.cross(direction, u1)

        # Random sampling within a circle (uniform disk sampling)
        rand_r = np.sqrt(np.random.rand(POINTS_PER_DISK)) * radius
        rand_theta = np.random.rand(POINTS_PER_DISK) * 2 * np.pi
        x_local = rand_r * np.cos(rand_theta)
        y_local = rand_r * np.sin(rand_theta)

        # Transform to global coordinates
        disk_points = np.array([
            center + x * u1 + y * u2
            for x, y in zip(x_local, y_local)
        ])

        # Plot sampled points in the disk
        ax.scatter(disk_points[:, 0], disk_points[:, 1], disk_points[:, 2], color=footprint_colors[beam_idx], s=5, alpha=0.2)

# Plot beam directions as dashed lines
for angle in zenith_angles_rad:
    dz = np.sin(angle)
    dy = np.cos(angle)
    dx = 0
    direction = np.array([dx, dy, dz])
    direction /= np.linalg.norm(direction)
    endpoint = 50 * direction
    ax.plot([0, endpoint[0]], [0, endpoint[1]], [0, endpoint[2]], linestyle='--', color='gray')

# Labels and settings
ax.set_xlabel('X (meters)')
ax.set_ylabel('Y (meters)')
ax.set_zlabel('Z (meters)')
ax.set_title('3D LiDAR Beam Paths with Solid Footprint Disks (Random Sampled Points)')
ax.set_box_aspect([1, 2, 1])
plt.tight_layout()
plt.show()
