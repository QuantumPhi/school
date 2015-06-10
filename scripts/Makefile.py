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

def build(id):
    # Targets:
    #   Fuzzy file matching (GH: seatgeek/fuzzywuzzy)
    #   Keep JSON/YAML file for config of individual files (Git LFS will store files, fetch to disk, then compile)
    print colored.red("NOT IMPLEMENTED")
    
def clean():
    i = 0
    for ext in open(".gitignore"):
        m = match_files(id=ext.strip(), dir=[".git"], file=["*.sublime-workspace"])
        for n in m:
            print "%s %s" % (colored.yellow("Deleted:"), n)
            os.remove(n)
            i += 1
    print colored.red("Deleted %d file%s" % (i, "" if i == 1 else "s"))

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--clean", action="store_true")
args = parser.parse_args()

if args.clean:
    clean()