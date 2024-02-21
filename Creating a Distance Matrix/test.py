import numpy as np
from scipy.spatial.distance import pdist, squareform

# Coordinates of points
points = np.array([[1, 2], [3, 4], [5, 6]])

# Calculate pairwise distances
distance_matrix = squareform(pdist(points))

print("Coordinates of points:")
print(points)
print("\nDistance Matrix:")
print(distance_matrix)
