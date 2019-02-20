#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 3"""


import argparse
import csv
import datetime
import re
import urllib2


def downloadData(url=str):
    """This function opens an inputed url and return the result to the caller.

    Args:

        url (str): A string that is a URL address.

    Returns:

        file object (various): A file object assigned to the variable
        downloadcsvfie.

    Example:

        >>> downloadData(
        'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv')
        <addinfourl at 140145322261104 whose fp = <socket._fileobject object at
        0x7f76202c78d0>>
    """
    downloadcsvfile = urllib2.urlopen(url)
    return downloadcsvfile


def processData(downloadcsvfile):
    """This function takes a variable that has an assigned file object to it,
       then parses the data for particular values.

    Args:

        downloadcsvfile (file object): A file downloaded from a URL by the
        downloadData() function.

    Returns:

        3 str:

            str 1: returns a string that states the results of the parsed file
            objectdownloadcsvfile. It reveals the percentage of hits on a site
            that were for image request, howmany hits in total the site recived,
            and what was the most popular web browser used to acces the site, and
            how many times it was used.
            The results of local variables: percentageimagehits
                                            lines
                                            browser_name
                                            popular

            Formated in this order, into the string:
                "Image requests account for {}% of todays total {} hits. {} was
                the most used web browser accessing the site with {} hits."

            str 2: a string that states:
                ********** Extra Credit **********

            str 3: Additionaly, several lines of strings of hits per hour,
            sorted by number of hits, from high to low, are printed to screen.

    Example:

        >>> test1 = downloadData(
        "http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv")
        >>> processData(test1)
        Image requests account for 78.77% of todays total 10000 hits.
        Chrome was the most used web browser accessing the site with 4042 hits.
        ********** Extra Credit **********
        Hour 04 has 1813 hits.
        Hour 01 has 1808 hits.
        Hour 03 has 1797 hits.
        Hour 02 has 1795 hits.
        Hour 00 has 1793 hits.
        Hour 05 has 994 hits.
        Hour 23 has 0 hits.
        Hour 22 has 0 hits.
        Hour 21 has 0 hits.
        Hour 20 has 0 hits.
        Hour 19 has 0 hits.
        Hour 18 has 0 hits.
        Hour 17 has 0 hits.
        Hour 16 has 0 hits.
        Hour 15 has 0 hits.
        Hour 14 has 0 hits.
        Hour 13 has 0 hits.
        Hour 12 has 0 hits.
        Hour 11 has 0 hits.
        Hour 10 has 0 hits.
        Hour 09 has 0 hits.
        Hour 08 has 0 hits.
        Hour 07 has 0 hits.
        Hour 06 has 0 hits.
    """
    reader = csv.reader(downloadcsvfile)
    lines = 0
    imagehits = 0

    firefox = ['Firefox', 0]
    chrome = ['Chrome', 0]
    ie = ['Internet Explorer', 0]
    safari = ['Safari', 0]

    dateformat = '%Y-%m-%d %H:%M:%S'
    dict_times = {hour: 0 for hour in range(0, 24)}

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

        date = datetime.datetime.strptime(row[1], dateformat)
        dict_times[date.hour] = dict_times[date.hour] + 1
        sorted_times = sorted(dict_times.items(), key=lambda kv: kv[1])
        sorted_times.reverse()

    browser_totals = [chrome, safari, ie, firefox]
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

    print '*' * 10, 'Extra Credit', '*' * 10
    for time in sorted_times:
        print'Hour %02d has %s hits.' % (time[0], time[1])


def main():
    """ This function combines the downloadData() and processData()
        into a single function to be run on the command line.

        main() dowloads a file from a provided --url, processes the data,
        then returns the results of the processData() function.

        If an impropper --url is input, an error message is raised and the
        program exits.

    Exsample:

        $ python Assignment3.py --url http://s3.amazonaws.com/cuny-is211-
        spring2015/weblog.csv
        Image requests account for 78.77% of todays total 10000 hits.
        Chrome was the most used web browser accessing the site with 4042 hits.
        ********** Extra Credit **********
        Hour 04 has 1813 hits.
        Hour 01 has 1808 hits.
        Hour 03 has 1797 hits.
        Hour 02 has 1795 hits.
        Hour 00 has 1793 hits.
        Hour 05 has 994 hits.
        Hour 23 has 0 hits.
        Hour 22 has 0 hits.
        Hour 21 has 0 hits.
        Hour 20 has 0 hits.
        Hour 19 has 0 hits.
        Hour 18 has 0 hits.
        Hour 17 has 0 hits.
        Hour 16 has 0 hits.
        Hour 15 has 0 hits.
        Hour 14 has 0 hits.
        Hour 13 has 0 hits.
        Hour 12 has 0 hits.
        Hour 11 has 0 hits.
        Hour 10 has 0 hits.
        Hour 09 has 0 hits.
        Hour 08 has 0 hits.
        Hour 07 has 0 hits.
        Hour 06 has 0 hits.
    """
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
