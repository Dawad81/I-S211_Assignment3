#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 3"""


import argparse
import csv
import datetime
import re
import urllib2



url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'


def downloadData(url=str):
    """Docstring"""
    downloadcsvfile = urllib2.urlopen(url)
    return downloadcsvfile

test1 = downloadData("http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv")

def processData(downloadcsvfile):
    """Docstring"""
    reader = csv.reader(downloadcsvfile)
    lines = 0
    imagehits = 0

    firefox = ['Firefox', 0]
    chrome = ['Chrome', 0]
    ie = ['Internet Explorer', 0]
    safari = ['Safari', 0]

    dateFormat = '%Y-%m-%d %H:%M:%S'
    times = {i: 0 for i in range(0, 24)}


    for row in reader:
        lines += 1
        if re.search(
                r"[^\s]+(?=\.(jpg|gif|png|jpeg))", row[0], re.I):
            imagehits += 1

        percentageimagehits = (float(imagehits) / lines) * 100

        if re.search("firefox", row[2], re.I):
            firefox[1] += 1
        elif re.search(r"MSIE", row[2]):
            ie[1] += 1
        elif re.search(r"Chrome", row[2]):
            chrome[1] += 1
        elif re.search(r"Safari", row[2]) and not re.search(
                "Chrome", row[2]):
            safari[1] += 1

        date = datetime.datetime.strptime(row[1], dateFormat)
        times[date.hour] = times[date.hour] + 1
        sorted_times = sorted(times.items())
        sorted_times.reverse()

    browser_totals = [chrome, ie, safari, firefox]
    popular = 0
    browser_name = ''
    for num in browser_totals:
        if num[1] > popular:
            popular = num[1]
            browser_name = num[0]
        else:
            continue

    result = 'Image requests account for {}% of todays total {} hits.\n{} was '\
             'the most used web browser accessing the site with {} '\
             'hits.'.format(percentageimagehits, lines, browser_name, popular)

    print result
    print '*' * 10,('Extra Credit'),'*' * 10


    for i in sorted_times:

        print'Hour %02d has %s hits.' % (i[0], i[1])
    print times

test2 = processData(test1)

def main():
    """Docstring"""
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
