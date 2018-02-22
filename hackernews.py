#!usr/bin/env python3.6

# Date: 02-22-18, Feb ~ 22nd 2018 | Synchronocy
# Project: Hacker News Scraper
# Just testing my scraper on multiple websites
# IDLE Python 3.6 64-bit

import requests
counter = 1
        
filename = 'recentarticles.txt'
def removedupes(inputfile, outputfile):
        lines=open(inputfile, 'r').readlines()
        lines_set = set(lines)
        out=open(outputfile, 'w')
        for line in lines_set:
                out.write(line)
        print('\nScan completed.\nRemoved any/all dupes.')
        
while 1:
    #pool = ThreadPool(800)
    src = requests.get('https://news.ycombinator.com/news?p='+str(counter)).text
    counter += 1
    #<h2><a href=" "
    links = src.split('<td class="title"><a href="')[1:]
    for link in links:
        link = link.split('"')[0]
        print(link)
        with open(filename,"a") as handle:
            handle.write(link + '\n')
            handle.close()
        removedupes(filename,filename)
        
