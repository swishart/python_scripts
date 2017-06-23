import glob
import os

rootdir = os.getcwd()

def check_string(filename):
    #no need to pass arguments to function if you're not using them
    w = " A BibTeX formatted list of references used in this run has been written to"
    #open the file using `with` context manager, it'll automatically close the file for you
    with open(filename) as f:
        found = False
        for line in f:  #iterate over the file one line at a time(memory efficient)
            if w in line:    #if string found is in current line then print it
                return True
       

def successful_jobs(print_jobs):
	successful_directories = []

	dirs = glob.glob(rootdir + os.sep + "*/")
	for dir in dirs:
		error_files=glob.glob(dir+"Si.000*.err")
		slurm_file=glob.glob(dir+"slurm*")
		castep_file=glob.glob(dir+"Si.castep")

		# Only required for /Users/SarahWishart/_drives/tinis/database/170614_singlepoint_temperature_calculations/
		if len(castep_file) == 0:
				castep_file=glob.glob(dir+"Si_out.castep")

		# If castep file exists check if it's finished or has errored in any way
		if len(castep_file) != 0:
			if error_files:
				if print_jobs == 1: 
					 print "Xerr = "+dir
			elif slurm_file and os.path.getsize(slurm_file[0]) > 0:
				if print_jobs == 1: 
	   				 print "Xslurm = "+dir
			# If the string "Bibtex formatted appears, the calculation has finished"	
			elif check_string(castep_file[0]):
				if print_jobs == 1: 
					 print "S  = "+dir
				successful_directories += [dir]
			else:
				if print_jobs == 1: 
					print "-running- = "+dir
		else:
			if print_jobs == 1: 	
				print "-yet to run- = "+dir

	return successful_directories