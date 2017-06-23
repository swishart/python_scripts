# Go through each directory and collect the following information
def get_cell(filename):
    import ase
    from ase import io
 

    data = ase.io.read(filename)
    cell = data.get_cell()

    return cell

# Create array of attributes from dirs in rootdir
def plot_boxsize(xaxis, xend, rootdir):
    import os
    import ase
    from ase import io
    import glob
    from ase.io.castep import read_castep_new
    import subprocess
    import numpy as np
    import matplotlib.pyplot as plt

    files = glob.glob(rootdir + "*/*." + xend)
   
    atoms = [read_castep_new(file) for file in sorted(files)]
    
    print atoms

    boxsize = np.array([])
    energy = np.array([])
    for i in range(0,4):#len(atoms)):
        boxsize = np.append(boxsize, atoms[i].get_cell()[0][0])
        energy = np.append(energy, [atoms[i].get_total_energy()])
    print boxsize
    print energy


    graph = plt.plot(boxsize,energy)
    #plt.show()

    # Create array of attributes from dirs in rootdir
def plot_kpoints(xend, rootdir):
    import os
    import ase
    from ase import io
    import glob
    #from ase.io.castep import read_castep_new
    import subprocess
    import numpy as np
    #import matplotlib.pyplot as plt

    files = glob.glob(rootdir + os.sep + "*/*." + xend)
    dirs = glob.glob(rootdir + os.sep + "*/")
    print files
    
    kpoints=[]
    #atoms = [read_castep_new(file) for file in sorted(files)]
    atoms = [ase.io.read(file,format="castep-castep") for file in sorted(files)]
    
    print atoms

    for dir in sorted(dirs):
        os.chdir(dir)
        kpoints += [os.path.relpath(".","..")] 
        os.chdir(rootdir)

    print kpoints
    #print atoms


    #energy = np.array([])
    
    energy = []
    for atom in atoms:
        print atom
        print atom.get_kinetic_energy()
        #energy = np.append(energy, [atoms[i].get_total_energy()])
        print atom.get_total_energy()
        energy += [atom.get_total_energy()]
    print kpoints
    print energy


    #graph = plt.plot(kpoints,energy)
    #plt.show()

# Copy pbs files into dirs and submit jobs to tinis
def copy_and_run_pbs(rootdir, dirlist, pbsfile):
    from shutil import copyfile
    import os
    import subprocess

    for dir in dirlist:
        copyfile(rootdir+pbsfile, dir+os.sep+pbsfile)
        os.chdir(dir)
        print(os.getcwd())
        print ("msub "+pbsfile)
        subprocess.call("msub "+pbsfile, shell=True)
        os.chdir(rootdir)
        print(os.getcwd())

# Function to create a file from a template swapping "TEMP" with input.
def file_from_tempfile(tempfile, newfile, new_val,temp, rootdir):
    
    import os
    import glob

    with open(tempfile, "rt") as fin:
        with open(newfile, "wt") as fout:
            for line in fin:
                fout.write(line.replace(temp, new_val))

    fout.close()
    fin.close()



#Make directories with the following names
def mkdirs(rootdir, names):
    import os

    for name in names:
        print (rootdir+name)
        os.mkdir(rootdir + name)


def copy_file(newfilepath, file):
    import os
    from shutil import copyfile

    print("New file path = "+newfilepath)
    copyfile(file, newfilepath)


# add some lines to file
def add_lines(filename):
    with open(filename,"a") as file:
        file.write("\nsymmetry_generate \nkpoints_mp_grid = 4 4 4")

    file.close()


# take first 30 atoms and create new cell file
def forty_atoms(filepath,newfilepath):

    with open(filepath, "rt") as fin:
        thirtyatoms=fin.readlines()[0:40] # including 10 lines of headers
        with open(newfilepath, "wt") as fout:
            for line in thirtyatoms:
                fout.write(line)
            fout.write("%ENDBLOCK POSITIONS_ABS")

    fout.close()
    fin.close()




