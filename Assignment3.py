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
        #if re.search(r"jpg|png|gif", line[0]):
        if re.search(r"[^\s]+(?=\.(jpg|gif|png))", line[0]):
            imagehits += 1
        #print line
        lines += 1

    percentageimagehits = (float(imagehits) / lines) * 100
    print percentageimagehits 
    
        
#if re.search(r"[^\s]+(?=\.(jpg|gif|png))")

#print processData(test1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="Enter a URL to begin.", required=True)
    args = parser.parse_args()
    try:
        csvData = downloadData(args.url)
    except:
        print 'An error has occured session terminated.\n\
        Exiting the program......Good Bye.'
        raise SystemExit
    else:
        processData(csvData)




if __name__ == '__main__':
    main()
