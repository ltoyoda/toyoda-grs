from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob
import math


# def compute(a, b, c, d, e, f, g, h, i, file):
#     """Return filename of plot of the damped_vibration function."""
#     print (os.getcwd())
    # y = [0, a, b, c, d, e, f, g, h]
    # ya = 2.198[(a-b)*(a-b)]

#     print (compute(1, 1, 1, 1, 0.5, 0.25, 0, 0, 0, "variog"))
a = 1
b = 1
c = 1
d = 1
e = .5
f = .25
g = 0
h = 0
i = 0

y_new2 = [(a-b), (a-c), (a-d), (a-e), (a-f), (a-g), (a-h), (a-i), (a-i)]
# y_new = [0, a, (a+b), (a+b+c), (a+b+c+d), (a+b+c+d+e), (a+b+c+d+e+f), (a+b+c+d+e+f+g), (a+b+c+d+e+f+g+h)]
# print y_new
t = [100, 500, 1000, 5000, 10000, 15000, 20000, 25000, 30000]
# new_y = [ a, b, c, d, e, f, g, h,i]
# y = [a, b, c, d, e, f, g, h, i]

sill = 45.0;
range2 = 150;
nugget = .1;
h = y_new2;

exponent = []
gauss = []
spherical = []

for m in range(len(h)):
    exp_1 = (sill-nugget)*(1-math.exp(-3*h[m]/range2))+nugget;
    exponent.append(exp_1)
    gss_1 = (sill-nugget)*(1-math.exp(-3*h[m]/range2**2))+nugget;
    gauss.append(gss_1)
    # sphe_1 = (sill-nugget)*(3*math.h[m]/(2*range) - h[m]**(3/(2*range2**3)));
    # sperical.append(sphe_1)

def opt( fct, x, y, C0, parameterRange=None, meshSize=1000 ):
    if parameterRange == None:
        parameterRange = [ x[1], x[-1] ]
    mse = np.zeros( meshSize )
    a = np.linspace( parameterRange[0], parameterRange[1], meshSize )
    for i in range( meshSize ):
        mse[i] = np.mean( ( y - fct( x, a[i], C0 ) )**2.0 )
    return a[ mse.argmin() ]

def spherical( h, a, C0 ):
    '''
    Spherical model of the semivariogram
    '''
    # if h is a single digit
    if type(h) == np.float64:
        # calculate the spherical function
        if h <= a:
            return C0*( 1.5*h/a - 0.5*(h/a)**3.0 )
        else:
            return C0
    # if h is an iterable
    else:
        # calcualte the spherical function for all elements
        a = np.ones( h.size ) * a
        C0 = np.ones( h.size ) * C0
        return map( spherical, h, a, C0 )

def cvmodel( P, model, hs, bw ):
    '''
    Input:  (P)      ndarray, data
            (model)  modeling function
                      - spherical
                      - exponential
                      - gaussian
            (hs)     distances
            (bw)     bandwidth
    Output: (covfct) function modeling the covariance
    '''
    # calculate the semivariogram
    sv = SV( P, hs, bw )
    # calculate the sill
    C0 = C( P, hs[0], bw )
    # calculate the optimal parameters
    param = opt( model, sv[0], sv[1], C0 )
    # return a covariance function
    covfct = lambda h, a=param: C0 - model( h, a, C0 )
    return covfct

sp = cvmodel( P, model=spherical, hs=np.arange(0,10500,500), bw=500 )
plot( sv[0], sv[1], '.-' )
plot( sv[0], sp( sv[0] ) ) ;
title('Spherical Model')
ylabel('Semivariance')
xlabel('Lag [m]')
savefig('semivariogram_model.png',fmt='png',dpi=200)

plt.figure()  # needed to avoid adding curves in plot
plt.plot(t, h, 'ro')
plt.plot(t, exponent)
plt.plot(t, gauss)
plt.title('Semivariogram')
plt.xlabel('Distance Lag (meters)')
plt.ylabel('Semivariance (gamma)')
plt.ylim([0, 1.5])
plt.grid(True)


plt.show()
# if not os.path.isdir('static'):
#     os.mkdir('static')
# else:
#     # Remove old plot files
#     for filename in glob.glob(os.path.join('static', '*.png')):
#         os.remove(filename)

# Use time since Jan 1, 1970 in filename in order make
# a unique filename that the browser has not chached
#    plotfile = os.path.join('static', str(time.time()) + '.png')
# plotfile = os.path.join('static', file + '.png')
#
# plt.savefig(plotfile)
# return plotfile

# if __name__ == '__main__':
#     print (compute(1, 1, 1, 1, 0.5, 0.25, 0, 0, 0, "variog"))
#
#
#     # <!--<img src="{% get_static_prefix %}{{ result }}" width=500>-->