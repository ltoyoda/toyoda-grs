__author__ = 'Toyoda'

import math
import time
import numpy as np
# from numpy import exp, cos, linspace
# import matplotlib.pyplot as plt
import os, time, glob
# from django.contrib.gis.geos.base import numpy

def compute(r):
    return math.sin(r)

def soma(r, s, t, u):
    return (r + s + t + u)

def mean(r, s, t, u):
    ans = ((r + s + t + u)/4.)
    # out_file_nm = str('outputfile_from_compute.txt')
    # fh = open(out_file_nm, 'w')
    # fh.write('Testing output file in compute.py for program APK, app plot \n\n')
    # fh.write('Mean:  ')
    # fh.write(str(ans) +'\n')
    # fh.close()
    return (ans)

def write_txt(r,s,t,u,filename):
        out_file_nm = str( filename + '.txt')
        fh = open(out_file_nm, 'w')
        # fh.write('Testing output file in views (index_math_2p) for program APK, app plot \n\n')
        fh.write('Testing output file in compute.py for program APK, app plot \n\n')
        fh.write('Input 1:  ')
        fh.write(str(r) +'\n')
        fh.write('Input 2:  ')
        fh.write(str(s) +'\n')
        fh.write('Input 3:  ')
        fh.write(str(t) +'\n')
        fh.write('Input 4:  ')
        fh.write(str(u) +'\n\n')
        fh.write('Sum:  ')
        fh.write(str(soma(r, s, t, u)) +'\n')
        fh.write('Mean:  ')
        fh.write(str(mean(r, s, t, u)) +'\n')
        fh.write('Sin of input 1:  ')
        fh.write(str(compute(r)) +'\n')
        fh.close()
        return out_file_nm
#############################################################
# from numpy import exp, cos, linspace
# import matplotlib.pyplot as plt
# import os, time, glob
#
# def damped_vibrations(t, A, b, w):
#     return A*exp(-b*t)*cos(w*t)
#
# def compute2(A, b, w, T, resolution=500):
#     """Return filename of plot of the damped_vibration function."""
#     print (os.getcwd())
#     t = linspace(0, T, resolution+1)
#     y = damped_vibrations(t, A, b, w)
#     plt.figure()  # needed to avoid adding curves in plot
#     plt.plot(t, y)
#     plt.title('A=%g, b=%g, w=%g' % (A, b, w))
#     if not os.path.isdir('static'):
#         os.mkdir('static')
#     else:
#         # Remove old plot files
#         for filename in glob.glob(os.path.join('static', '*.png')):
#             os.remove(filename)
#     # Use time since Jan 1, 1970 in filename in order make
#     # a unique filename that the browser has not chached
#     plotfile = os.path.join('static', str(time.time()) + '.png')
#     plt.savefig(plotfile)
#     # return plotfile
#     return (plt.show())

#
# if __name__ == '__main__':
#     print compute(20)
#     print soma(20,3,5,8)
#     print (compute2(1, 0.1, 1, 20))

    # x = [5, 10, 50, 100]
    # y = [20,3,5,8]
    # plt.plot(x, y)
    # plt.title('Testing plot')
    # plt.xlabel('Number of Points')
    # plt.grid(True)
    # plt.ylabel('Running time')
    # plt.show()