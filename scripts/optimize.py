import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.optimize as o
from os.path import expanduser

set = pd.read_csv(expanduser("~/git/school/2015-2016/Physics/Spaghetti_Lab/data.dat"), index_col=0, sep="\s*").to_records()
print set
fun = lambda k, x: k[0]*(k[1]*x+k[2])**2+k[3]

def err(k):
    return sum(((fun)(k, set[i][0]) - set[i][4])**2 for i in xrange(len(set)))

guess = [1., 1., 1., 1.]

opt = o.minimize(err, guess, method="L-BFGS-B")["x"]

x = [val[0] for val in [row for row in set]]
y = [val[6] for val in [row for row in set]]
z = np.arange(min(x), max(x), 0.00001)

print opt
print err(opt)

plt.plot(z, fun(opt, z), linewidth=1, c="red")
for i in xrange(len(x)):
    plt.scatter(x[i], y[i], s=10, c="blue")

plt.show()
