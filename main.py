from PIL import Image
import numpy as np
import pyvista as pv

# Step 1: Load and process the image
try:
    image = Image.open("input.jpg").convert("L")
except Exception as e:
    print("❌ Failed to open image:", e)
    exit()

# Step 2: Resize for faster processing
image = image.resize((200, 200))
pixels = np.array(image)

# Step 3: Create X, Y, Z coordinates
x = np.linspace(0, 1, pixels.shape[1])
y = np.linspace(0, 1, pixels.shape[0])
x, y = np.meshgrid(x, y)
z = pixels / 255.0  # Normalize brightness to [0,1]

# Create and show 3D surface
grid = pv.StructuredGrid(x, y, z)

# Convert to PolyData before export
surf = grid.extract_surface()

# Export to .obj and .stl formats
try:
    surf.save("output_model.obj")
    surf.save("output_model.stl")
    print("✅ 3D model saved as .obj and .stl")
except Exception as e:
    print("❌ Failed to save 3D model:", e)

# Show the model
plotter = pv.Plotter()
plotter.add_mesh(grid, cmap="gray")
plotter.show()
