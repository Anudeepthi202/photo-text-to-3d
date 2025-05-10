# app.py

import open3d as o3d
import pyvista as pv

# Create a sample 3D object (e.g., a cube)
cube = o3d.geometry.TriangleMesh.create_box()

# Print info about the cube
print("3D Cube created:")
print(cube)

# You can add visualization or Flask app here next
o3d.visualization.draw_geometries([cube])