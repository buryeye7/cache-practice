#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import MySQLdb
import urllib.request
import sys
import random

def get_page(page):
    port = 5000
    with urllib.request.urlopen('http://localhost:%s/%s'%(port, page)) as url:
        web = url.read()
        print(web)

if __name__ == "__main__":
    start_page = int(sys.argv[1])
    end_page = int(sys.argv[2])
    while(True):
        get_page(random.randrange(start_page, end_page))
