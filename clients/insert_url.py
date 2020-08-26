import MySQLdb
import urllib.request
import sys


def insert_list(page):
    port = 5000
    url = "http://charsyam.wordpress.com/%s"%page
    insert_page = "http://172.20.50.198:%s/create/%s"%(port, url)
    web = urllib.request.urlopen(insert_page)

if __name__ == "__main__":
    port = 5000
    for i in range(int(sys.argv[1]), int(sys.argv[2])):
        insert_list(i)
