# Arjun Sabnis
# Monte Carlo simulation of percolation
# Created on 9/6/2018

from math import sqrt
from percolation import Percolation
from union_find import UnionFind
from sys import argv


def stats(size, trials):
    samples = []
    total = 0.0

    for i in range(trials):
        p1 = Percolation(size)
        result = p1.threshold()
        samples.append(result)
        total = total + result

    mean = total/float(trials)
    
    stdev = 0.0
    for i in range(trials):
        stdev += (samples[i]-mean)**2

    stdev = sqrt(stdev/float(trials-1))
    
    confLo = (mean - 1.96*stdev)/sqrt(float(trials))
    confHi = (mean + 1.96*stdev)/sqrt(float(trials))
    
    print "Sample Mean                      = %f" % mean
    print "Standard Deviation               = %f" % stdev
    print "95%% Confidence Interval         = [%f, %f]" % (confLo, confHi)


stats(int(argv[1]), int(argv[2]))
