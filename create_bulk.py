from functions import *
from completed_jobs import *
from castep_to_potfit import *
#import numpy as np
import glob
from shutil import copyfile
import os
import ase 
from ase import io

#rootdir = "/home/theory/phukew/castep/Si2/PBE/kpoints/"
#rootdir="/Users/SarahWishart/_drives/tinis/castep/Si2/PBE/kpoints/"
#rootdir="/Users/longbottom/_drives/tinis/castep/Si2/PBE/kpoints/"
xend="castep"
pbsfile="Si.pbs"

rootdir = os.getcwd()

# x =  5.43100
# y = 24.07325

# print rootdir
# names = []
# coordsxy = []
# for i in range(1,5):
# 	coordsxy += [x*((i*0.1)+1),y*((i*0.1)+1)]
# 	names += [str(i)]

# print names
# print coordsxy

# cellfiles = glob.glob("*/Si.castep")
# slurmfiles = glob.glob("*/slurm*")
#cellfiles = [rootdir+os.sep+"Si_bulk_T300_NVE_tersoff_905.cell"]

dirs = successful_jobs(print_jobs=0)

potfiles = []
for dir in dirs:
	file = dir+"Si.castep"
	data = ase.io.read(file)
	# print data
	# print data.get_forces()
	potname = os.path.basename(os.path.dirname(file))+".pot_config"
	print potname
	potfiles += [potname]
	#potfit_input_file(potname,data)

final_input_file(potfiles, "Si_512atom_bulk_temperature_configs.pot_config")

pbsfile="Si.pbs"
paramfile="Si.param"

# for file in cellfiles:
# 	print file
# 	base = os.path.basename(file)
# 	dirname = os.path.splitext(base)[0]
# 	folder = os.path.dirname(file)
# 	print folder
# 	castepfile = rootdir+os.sep+folder+os.sep+"Si.castep"
# 	print castepfile
# 	os.makedirs(rootdir+os.sep+str(dirname))
# 	copyfile(file, rootdir+os.sep+dirname+os.sep+base)
# 	file_from_tempfile(file, rootdir+os.sep+dirname+os.sep+"Si.cell", "Si", "X", rootdir)
# 	copyfile(rootdir+os.sep+pbsfile, rootdir+os.sep+dirname+os.sep+pbsfile)
# 	copyfile(rootdir+os.sep+paramfile, rootdir+os.sep+dirname+os.sep+paramfile)
# 	add_lines(rootdir+os.sep+dirname+os.sep+"Si.cell")


# 	for name in names:
# 		copy_file(rootdir+os.sep+name+os.sep+os.path.basename(file),file)
# 		file_from_tempfile(file,rootdir+os.sep+name+os.sep+os.path.basename(file)+"temp",str(x*((int(name)*0.1)+1)), "XVAL" ,rootdir)
# 		file_from_tempfile(rootdir+os.sep+name+os.sep+os.path.basename(file)+"temp",rootdir+os.sep+name+os.sep+os.path.basename(file),str(y*((int(name)*0.1)+1)), "YVAL" ,rootdir)
# 	#print get_cell(file)


# temp_files = glob.glob(rootdir + os.sep+ "*/*.*temp")
# print temp_files

# for file in temp_files:
# 	os.remove(file)

# # #for dir in dirs:
# for name in names:
# 	for file in cell_files:
# 		newfile = rootdir+os.sep+name+"/Si_slab.cell"
# 		print file
# 		copy_file(newfile,file)
# #	add_lines(file, newfile)

# dirs = glob.glob(rootdir + os.sep + "Si_*/")
                                                          
# copy_and_run_pbs(rootdir + os.sep, dirs, pbsfile)

#plot_kpoints(xend, rootdir+os.sep)
#plot_attribute(1, "castep", rootdir)
#print (get_cell(rootdir+"10.0/Si_single.castep"))
