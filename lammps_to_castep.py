import ase
from ase import io
import glob
import os


files = glob.glob("Ni_*.xyz")
print files


for file in files:
	data = ase.io.read(file, index=':', format="xyz")
	base=os.path.basename(file)
	new_file=os.path.splitext(base)[0]
	print data

	ase.io.write(new_file+".cell", data)