#!/usr/bin/env python3

import sys
import urlshort
import random
import urllib
import numbers
import argparse
from urllib.request import urlopen
import urllib.request


# A nice website opener
class AppURLopener(urllib.request.FancyURLopener): 
    version = "Mozilla/5.0"
opener = AppURLopener()


# Parse command line input
parser = argparse.ArgumentParser(description="Generates random, valid nhentai links.")
parser.add_argument('-s', '--shorten', default=False, choices=[True, False], type=bool, help='If this parameter is passed generated link/s will be shortened just in case')
parser.add_argument('-n', '--number', default=1, type=int, help='Using this parameter you can select number of generated links.')
args = parser.parse_args()


# Functions
def mkurl(Shortening):              # <= Makes a url, may shorten it
    urlready = False
    while urlready != True:
        url = ("""https://nhentai.com/g/""" + str(random.randint(1,269000)))
        if urlcheck(url) != "404":
            urlready = True
        else:
            pass
    if Shortening == True:
        shortenedurl = urlshort.shorturl(url)
        return shortenedurl
    else:
        shortenedurl = url
        return shortenedurl

def urlcheck(url):                  # <= Checks if page exists
    resp = opener.open(url)
    resp = resp.geturl()
    resp = opener.open(resp)
    return resp.getcode()

def Sauce(Number, Shortening):      # <= Bundles everything up
    urls = ("")
    urls = list(urls)
    if Number == '':
        Number = 1
    while Number > 0:
        urls.append(mkurl(Shortening))
        Number -= 1
    urls = str(urls)
    return urls


# Main Script
    
def main():
    Number = ''
    Shortening = False
    if args.number:
        if isinstance(args.number, numbers.Number) == True:
            Number = args.number
        else:
            print("Please select a valid number bigger than 0.")
            sys.exit(2)
    if args.shorten:
        if args.shorten == True:
            print("Links are shortened.")
            Shortening = True
    print(Sauce(Number, Shortening))
        

if __name__ == '__main__':
    main()
