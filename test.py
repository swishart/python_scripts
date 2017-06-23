ovitoimport glob
import ase
from ase import io
import os

files = glob.glob("*.xyz")
print files

for file in files:
	data = ase.io.read(file, format="xyz")
	print data
	ase.io.write(os.path.splitext(file)[0]+".cell",data)

