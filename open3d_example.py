import open3d as o3d

# Create a simple point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector([
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
])

# Visualize it
o3d.visualization.draw_geometries([pcd])
