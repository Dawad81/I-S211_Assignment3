#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 3."""


import argparse
import csv
import re
import urllib2
from pprint import pprint

url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
        
def downloadData(url):
    downloadcsvfile = urllib2.urlopen(url)
    return downloadcsvfile

test1 = downloadData(url)

def processData(downloadcsvfile):
    reader = csv.reader(downloadcsvfile)
    lines = 0
    imagehits = 0
    for line in reader:
        #print line
        lines += 1
    return lines
        


#print pprint(processData(test1))
