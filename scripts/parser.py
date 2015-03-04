import csv
import numpy as np
from os.path import expanduser

def file_data(path):
    return [line.strip("\n").split("\t") for line in open(expanduser(path), "rb").readlines()[7:]]

def to_csv(dataset, fname):
    for i in xrange(len(dataset)):
        with open(expanduser("~/Documents/DATA/%s%d.csv") % (fname, i+1), "wb") as file:
            writer = csv.writer(file)
            for point in dataset[i]: (lambda w, p: w.writerow(p))(writer, point)

def avg(dataset):
    avg_set = np.zeros(dataset.shape[1:])
    for j in xrange(dataset.shape[1]):
        row = np.zeros(dataset.shape[2])
        for i in xrange(dataset.shape[0]):
            row = [row[k]+dataset[i][j][k] for k in xrange(len(row))]
        row = [row[k]/len(row) for k in xrange(len(row))]
        avg_set[j] = row
    return [avg_set]

dataset = np.asarray(file_data("~/Documents/DATA/foo1.txt"), np.float)
avg(np.array([dataset]))
print dataset
