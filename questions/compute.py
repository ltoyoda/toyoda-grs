from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob


def compute(a, b, c, d, e, f, g, h, i, file):
    """Return filename of plot of the damped_vibration function."""
    print (os.getcwd())
    # y = [0, a, b, c, d, e, f, g, h]
    # ya = 2.198[(a-b)*(a-b)]
    y_new2 = [(a-b), (a-c), (a-d), (a-e), (a-f), (a-g), (a-h), (a-i), (a-i)]
    # y_new = [0, a, (a+b), (a+b+c), (a+b+c+d), (a+b+c+d+e), (a+b+c+d+e+f), (a+b+c+d+e+f+g), (a+b+c+d+e+f+g+h)]
    # print y_new
    t = [100, 500, 1000, 5000, 10000, 15000, 20000, 25000, 30000]
    # new_y = [ a, b, c, d, e, f, g, h,i]
    # y = [a, b, c, d, e, f, g, h, i]


# sill=0.1;
# range=10^4;
# nugget=0;
# h = y_ew
# # h1=0:1000:3.5*10^5;
# # step=1;
#
# exponent=(sill-nugget)*(1-exp(-3*h/range))+nugget;
# gauss=(sill-nugget)*(1-exp(-(3*h/range)^2))+nugget;
# spherical= (sill-nugget)*(3*h/(2*range) - h^3/(2*range^3));


    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(t, y_new2, 'ro')
    plt.title('Variogram')
    plt.xlabel('Distance lag (meters)')
    plt.ylabel('Semivariance (gamma)')
    plt.ylim([0, 1.5])
    plt.grid(True)
    # if not os.path.isdir('static'):
    #     os.mkdir('static')
    # else:
    #     # Remove old plot files
    #     for filename in glob.glob(os.path.join('static', '*.png')):
    #         os.remove(filename)

    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
#    plotfile = os.path.join('static', str(time.time()) + '.png')
    plotfile = os.path.join('static', file + '.png')

    plt.savefig(plotfile)
    return plotfile

if __name__ == '__main__':
    print (compute(1, 1, 1, 1, 0.5, 0.25, 0, 0, 0, "variog"))


    # <!--<img src="{% get_static_prefix %}{{ result }}" width=500>-->