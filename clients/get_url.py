#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import MySQLdb
import urllib.request
from urllib.error import URLError 
import sys
import random

def get_page(page):
    port = 5000
    #with urllib.request.urlopen('http://172.20.50.198:%s/%s'%(port, page)) as url:
    url = urllib.request.urlopen('http://172.20.50.198:%s/%s'%(port, page))
    try:
        web = url.read()
        print(web)
    except OSError as ose:
        print("os exception occured ", ose)
    except URLError as urle:
        print("url exception occured ", urle)
    finally:
        url.close()

if __name__ == "__main__":
    start_page = int(sys.argv[1])
    end_page = int(sys.argv[2])
    while(True):
        get_page(random.randrange(start_page, end_page))
