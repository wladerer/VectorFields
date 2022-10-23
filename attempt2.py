import numpy as np
import pyvista as pv

nx = 20
ny = 15
nz = 5

origin = (-(nx - 1) * 0.1 / 2, -(ny - 1) * 0.1 / 2, -(nz - 1) * 0.1 / 2)
mesh = pv.UniformGrid(dims=(nx, ny, nz), spacing=(0.1, 0.1, 0.1), origin=origin)
x = mesh.points[:, 0]
y = mesh.points[:, 1]
z = mesh.points[:, 2]
vectors = np.empty((mesh.n_points, 3))
vectors[:, 0] = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
vectors[:, 1] = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
vectors[:, 2] = np.sqrt(3.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z)

mesh['vectors'] = vectors # add the vector data to the mesh

stream, src = mesh.streamlines('vectors', return_source=True, terminal_speed=0.0, n_points=200, source_radius=0.1)  

cpos = [(1.2, 1.2, 1.2), (-0.0, -0.0, -0.0), (0.0, 0.0, 1.0)] # camera position
stream.tube(radius=0.0015).plot(cpos=cpos)