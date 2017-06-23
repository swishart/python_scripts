import ase
from ase import io
import glob
import os


files = glob.glob("Si_bulk_NVE_T300_8atoms_*")
print files


for file in files:
	data = ase.io.read(file, index=':', format="xyz")
	print data
	ase.io.write(file+".cell", data)