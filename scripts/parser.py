import csv
import numpy as n
from os.path import expanduser

def file_data(path):
    return [[t, p, c] for t, p, c in [line.strip("\n").split("\t") for line in open(expanduser(path), "rb").readlines()[7:]]]

def to_csv(dataset, fname):
    for i in xrange(len(dataset)):
        with open(expanduser("~/Documents/DATA/%s%d.csv") % (fname, i+1), "wb") as file:
            writer = csv.writer(file)
            writer.writerow(["time", "pH", "conductivity"])
            for point in dataset[i]: (lambda w, p: w.writerow(p))(writer, point)

def avg(dataset):
    avg_set = n.zeros(dataset.shape[1:])
    t = 0
    p = 0
    c = 0
    for i in xrange(dataset.shape[1]):
        for j in xrange(dataset.shape[0]):
            t += dataset[j][i][0]
            p += dataset[j][i][1]
            c += dataset[j][i][2]
        t /= dataset.shape[0]
        p /= dataset.shape[0]
        c /= dataset.shape[0]
        avg_set[i] = [t, p, c]
        t = 0
        p = 0
        c = 0
    return [avg_set]

dataset = n.asarray([file_data("~/Documents/DATA/foo%d.txt" % (i+1)) for i in xrange(3)], n.float)
to_csv(dataset, "foo")
to_csv(avg(dataset), "avg")
