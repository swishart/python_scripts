import ase
from ase import io
import os
import glob

# Write potfit input file
def potfit_input_file(file, data):

	with open(file, "w+") as fout:
	    fout.write("#N "+str(len(data))+" 1\n")
	    fout.write("#C "+str(data.get_chemical_symbols()[0])+"\n")
	    fout.write("#X "+str(data.get_cell()[0][0])+" "+str(data.get_cell()[0][1])+" "+str(data.get_cell()[0][2])+"\n")
	    fout.write("#Y "+str(data.get_cell()[1][0])+" "+str(data.get_cell()[1][1])+" "+str(data.get_cell()[1][2])+"\n")
	    fout.write("#Z "+str(data.get_cell()[2][0])+" "+str(data.get_cell()[2][1])+" "+str(data.get_cell()[2][2])+"\n")
	    fout.write("#E "+str(data.get_total_energy()/len(data))+"\n")	
	    fout.write("#F \n\n")
	    for i in range (0,len(data)):
	    	fout.write("0 ")
	    	for j in range (0,3):
	    		fout.write(str(data.get_positions()[i][j])+" ")
	    	for j in range (0,3):
	    		fout.write(str(data.get_forces()[i][j])+" ")
	    	fout.write("\n")

	fout.close() 

# Create giant potfit input file
def final_input_file(files,final_filename):

	with open(final_filename,"a+") as fout:
		for file in files:
			with open(file,"rt") as fin:
				for line in fin:
					fout.write(line)
				fout.write("\n\n")
			fin.close()
	fout.close()


#castepfile_dir="/Users/SarahWishart/_drives/tinis/database/170404_8atoms_ref_data"

#files = glob.glob(castepfile_dir+os.sep+"*/*/*.castep")
#print files

# for file in files:
# 	filename = os.path.split(os.path.dirname(file))[1]
# 	print filename
# 	data = ase.io.read(file)
# 	potfit_input_file(filename+".potfit_in", data)


#files = glob.glob("*.potfit_in")
#print files

#final_input_file(files,"Si_bulk_master.config")




 # N natoms useforce
 # C type_0 type_1 type_2 ...
 # X boxx.x boxx.y boxx.z
 # Y boxy.x boxy.y boxy.z
 # Z boxz.x boxz.y boxz.z
 #* B_S x y z r
 #* B_O x y z
 #* B_A x y z
 #* B_B x y z
 #* B_C x y z
 #* W weight
 # E coh_eng
 #* S stress_xx stress_yy stress_zz stress_xy stress_yz stress_xz
 # F 
