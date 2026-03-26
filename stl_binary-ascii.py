import sys

#pip install numpy-stl, not just stl
from stl import mesh
import stl

if len(sys.argv) != 2:
    print('please provide an stl file to convert')
    sys.exit(1)

binary_stl = sys.argv[1]

# Load the binary STL file
binary_mesh = mesh.Mesh.from_file(binary_stl)

ascii_stl = binary_stl.replace('.stl', '_ascii.stl')

# Save the mesh as an ASCII STL file
binary_mesh.save(ascii_stl, mode=stl.Mode.ASCII)
