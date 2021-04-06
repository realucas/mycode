#!/usr/bin/env python3
#parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 #set counter for fail - start count from 0
#open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
#convert the file into a list of lines in memory
keystone_file_lines=keystone_file.readlines()
# loop over the list of lines
for line in keystone_file_lines:
    #check the ff: fail pattern in the line..
    if "-----] Authorization failed" in line:
        loginfail += 1 # increase loginfail by 1
print(f" The number of failed log in attemtps is {loginfail} ")
keystone_file.close() #close the file
