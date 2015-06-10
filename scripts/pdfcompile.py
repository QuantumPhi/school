# A little something I wrote to compile a bunch of pages from a book I found online.

import os
import urllib

from clint.textui import colored
from pyquery import PyQuery as pq

base_url = "http://digital.library.pitt.edu"
save_loc = os.path.expanduser("~/Documents/pdf_dump/")

if not os.path.isdir(save_loc):
    os.mkdir(save_loc)

first_page = 3
last_page = 235

print colored.red("Fetching pages...")
for i in xrange(first_page, last_page):
    print "%s %d" % (colored.yellow("Page:"), i-2)
    p = pq(url="%s/cgi-bin/t/text/pageviewer-idx?c=pittpress&cc=pittpress&idno=31735057896064&node=31735057896064%%3A1&frm=frameset&view=pdf&seq=%d" % (base_url, i))
    frames = p("frame")
    frame = [pq(f) for f in frames if pq(f).attr["name"] == "main"][0]
    urllib.urlretrieve("%s%s" % (base_url, frame.attr["src"]), os.path.expanduser("%s/pdf-%d.pdf" % (save_loc, i-2)))

print colored.red("Compiling pages...")
for i in xrange((last_page-first_page)/100):
    print "%s %d" % (colored.yellow("Batch:"), i+1)
    os.system("gswin64 -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=%sbatch-%d.pdf -sBATCH %s" % (save_loc, i, " ".join(["%spdf-%d.pdf" % (save_loc, j) for j in xrange(i*100+1, (i+1)*100+1)])))

print "%s %d" % (colored.yellow("Batch:"), (last_page-first_page)/100+1)
os.system("gswin64 -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=%sbatch-%d.pdf -sBATCH %s" % (save_loc, (last_page-first_page)/100, " ".join(["%spdf-%d.pdf" % (save_loc, i) for i in xrange(((last_page-first_page)/100)*100+1, last_page-first_page+1)])))

print "%s %s" % (colored.yellow("Batch:"), (last_page-first_page)/100+2)
os.system("gswin64 -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=%scdf.pdf -sBATCH %s" % (save_loc, " ".join(["%sbatch-%d.pdf" % (save_loc, i) for i in xrange((last_page-first_page)/100+1)])))


print colored.red("Cleaning files...")
print "%s %d-%d" % (colored.yellow("Pages:"), 1, (last_page-first_page))
for i in xrange(1, last_page-first_page+1):
    os.remove("%spdf-%d.pdf" % (save_loc, i))

print "%s %d-%d" % (colored.yellow("Batch:"), 1, (last_page-first_page)/100+2)
for i in xrange((last_page-first_page)/100+1):
    os.remove("%sbatch-%d.pdf" % (save_loc, i))

print colored.red("Finished")
print "%s %s" % (colored.yellow("Output:"), "%scdf.pdf" % (save_loc))
