import argparse
import fnmatch
import os

from clint.textui import colored
from time import sleep

def match_files(id, dir, file):
    match = []
    for root, dirnames, filenames in os.walk("."):
        filenames = fnmatch.filter(filenames, id)
        for filename in filenames:
            if not (any(os.path.commonprefix([root[2:], pattern]) for pattern in dir) or any(fnmatch.filter(filenames, pattern) for pattern in file)):
                match.append(os.path.join(root, filename))
    return match

# TODO(): Create system that automatically generates new year
# def new_year(args, ib=False):
#     courses = ["Math", "English"] + args
#     year = os.listdirs(".")
#     for courses in courses:
        

def build(id):
    # Targets:
    #   Fuzzy file matching (GH: seatgeek/fuzzywuzzy)
    #   Keep JSON/YAML file for config of individual files (Git LFS will store files, fetch to disk, then compile)
    print colored.red("NOT IMPLEMENTED")
    
def clean():
    i = 0
    ignored = ["*.aux","*.lof","*.log","*.lot","*.fls","*.out","*.toc","*.dvi","*.bbl","*.bcf","*.blg","*-blx.aux","*-blx.bib","*.brf","*.run.xml","*.fdb_latexmk","*.synctex.gz*","*.idx","*.html","*~"]
    for pattern in ignored:
        m = match_files(id=pattern, dir=[".git/"], file=[])
        for n in m:
            print "%s %s" % (colored.yellow("Deleted:"), n)
            os.remove(n)
            i += 1
    print colored.red("Deleted %d file%s" % (i, "" if i == 1 else "s"))

parser = argparse.ArgumentParser()
parser.add_argument("-b", action="store_true", help=argparse.SUPPRESS)
parser.add_argument("-c", action="store_true", help=argparse.SUPPRESS)
args = parser.parse_args()

if args.b:
    build()
elif args.c:
    clean()