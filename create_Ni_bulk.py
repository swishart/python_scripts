import ase 
from ase import io
from ase.build import bulk



nickel = bulk('Ni', 'fcc', a=3.524, cubic=True)
nickel = nickel * (3, 3, 3)

print nickel.get_number_of_atoms()

#ase.io.write("Ni_bulk_108_atoms.cell", nickel)


