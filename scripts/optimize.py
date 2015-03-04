import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as o
from os.path import expanduser

set = np.array([row for row in csv.reader(open(expanduser("~/Documents/DATA/avg1.csv")))]).astype(np.float)
fun = lambda k, x: k[0]*np.log(k[1]*x+k[2])+k[3]

def err(k):
    return sum(((fun)(k, set[i][1]) - set[i][2])**2 for i in xrange(len(set)))

guess = [1., 1., 1., 1.]

opt = o.minimize(err, guess, method="L-BFGS-B")["x"]

x = [val[1] for val in [row for row in set]]
y = [val[2] for val in [row for row in set]]
z = np.arange(min(x), max(x), 0.01)

print opt
print err(opt)

plt.plot(z, fun(opt, z), linewidth=1, c="red")
for i in xrange(len(x)):
    plt.scatter(x[i], y[i], s=10, c="blue")

plt.show()
