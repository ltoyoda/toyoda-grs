__author__ = 'Toyoda'

import sys
import compute

r = 0.0    # input
s = None   # output

# Input: float r
# Output: "Hello, World! sin(r)=..."

def get_input():
    """Get input data from the command line."""
    r = float(sys.argv[1])
    return r

def present_output(r):
    """Write results to terminal window."""
    s = compute.compute(r)
    print ('Hello, World! sin(%g)=%g' % (r, s))



present_output(2)