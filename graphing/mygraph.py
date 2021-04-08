#!/usr/bin/env python3
"""RLucas | Create your own graph """

import matplotlib.pyplot as plt
import numpy as np
#import os

#Pull filesystem utilization data from system, extract field for graph to txt or csv
#def getfsstat():
    #os.system("df -h > dfstat.txt") or os.system("df -h | awk '{print $1, $5 }' > dfstat.txt")


def main():
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
