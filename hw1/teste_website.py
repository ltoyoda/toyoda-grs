from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob
import math


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
t = [100, 500, 1000, 5000, 10000, 15000, 20000, 25000, 30000]

sill = 0.1
range2 = 10**4
# nugget = 0;
# h = y_new2;


fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

