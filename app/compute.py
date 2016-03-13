__author__ = 'Toyoda'

import math
import time

# from numpy import exp, cos, linspace
#  import numpy
# import matplotlib.pyplot
# import matplotlib.pyplot as plt
# import os, time, glob
import numpy as np

def compute(r):
    return math.sin(r)

def soma(r, s, t, u):
#    return math.sin(r)
    return (r + s + t + u)

def mean(r, s, t, u):
#    return math.sin(r)
    return ((r + s + t + u)/4.)



# if __name__ == '__main__':
#     print compute(20)
#     print soma(20,3,5,8)
#
#
#     x = [5, 10, 50, 100]
#     y = [20,3,5,8]
#     plt.plot(x, y)
#     plt.title('Testing plot')
#     plt.xlabel('Number of Points')
#     plt.grid(True)
#     plt.ylabel('Running time')
#     plt.show()
#
# if __name__ == "__main__":
#
#     print plotando(2,3,4,5)

    # print y
    # plt.plot(x, y)
    # plt.title('Extrapolated Running time of program DelaunayTriangulation')
    # plt.xlabel('Number of Points')
    # plt.grid(True)
    # plt.ylabel('Running time')
    # plt.show()

# if __name__ == '__main__':
#     print compute(20)

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
#     return plotfile
#
# if __name__ == '__main__':
#     print (compute2(1, 0.1, 1, 20))