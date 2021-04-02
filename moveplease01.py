#!/usr/bin/env python3
import shutil
import os

os.chdir('/home/student/mycode/') #Force python to start in the home directory

# Move the file or folder at the path source to path destination and return a string of the 
# absolute path of the new location. 

shutil.move('raynor.obj', 'ceph_storage/')

# Prompt the user for a new name for the kerrigan.obj file.
xname = input('What is the new name for kerrigan.obj? ')

# Rename the current kerrigan.obj file

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



