#!/usr/bin/env python3
"""RLucas | Create your own graph """

import matplotlib.pyplot as plt
import numpy as np
from subprocess import call
#import os

#Pull filesystem utilization data from system, extract field for graph to txt or csv
#def getfsstat():
    #os.system("df -h > dfstat.txt") or os.system("df -h | awk '{print $1, $5 }' > dfstat.txt")
def getfsdata():
    # issue our command to get filesystem usage
    with open("dfstat.tmp", "w") as dfstat:
        call(["df", "-h"], stdout=dfstat)
    # open the file, read out data line by line
    # remember, the first line is garbage! (stuff across the top)
    linecount = 0
    fsd = {}  # this is what we are going to return
    with open("dfstat.tmp", "r") as dfstat:
        for line in dfstat:
            if linecount == 0: # if we're on the first line in our data
                linecount += 1  # add 1 to linecount
                continue       # skip to the next line... we only want lines 2 through n
            line = line.split() # transform a STR into a LIST
            fsd[f"fs{linecount}"] = {"name": line[0], "percent": line[4].rstrip("%"), "mount": line[5]}
            #fsd[line[0]] = line[4].rstrip("%")  # fsd["udev"] = "0"
            linecount += 1  # add 1 to linecount
    return fsd


def main():
    print(getfsdata())
    # Fixing random state for reproducibility
    np.random.seed(19680801)


    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Data Hardcode until pulling current data is figured out
    filesys = ('udev', 'tmpfs', '/dev/sda1', 'tmpfs', 'tmpfs', 'tmpfs', '/dev/sda15')
    y_pos = np.arange(len(filesys))
    utilization = 3 + 10 * np.random.rand(len(filesys))
    error = np.random.rand(len(filesys))

    ax.barh(y_pos, utilization, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(filesys)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Percent utilization')
    ax.set_title('Filesystem')
    #plt.show()
    plt.savefig("/home/student/mycode/graphing/mygraph.png")
    plt.savefig("/home/student/static/mygraph.png")
main()
