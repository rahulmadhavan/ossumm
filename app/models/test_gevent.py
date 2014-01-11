from httplib2 import Http
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import gevent
import threading
import urllib2



class urlFetcher (threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
        self.images = []
    def run(self):
        result = fetch_images_with_headers(self.url)
        for image in result:
            self.images.append(image)


def fetch(url,get_headers):
    resp, content = Http().request(url,"GET",headers= get_headers)
    # req = urllib2.Request(url, headers = get_headers)
    # response = urllib2.urlopen(req)
    # content = response.read()
    return content

def parse_image(article): return article.find('img')

def parse_content(content):
    soup = BeautifulSoup(content,"lxml")
    result = map(parse_image,soup.find_all('article'))
    return result


def fetch_images(url,get_headers):
    content = fetch(url,get_headers)
    images = parse_content(content)
    return images


def fetch_images_with_headers(url):
    get_headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/31.0.1650.63 Safari/537.36'}
    return fetch_images(url,get_headers)


def synchronous(urls):
    map(fetch_images_with_headers,urls)


def asynchronous(urls):
    threads = []
    for url in urls:
        threads.append(gevent.spawn(fetch_images_with_headers, url))
    gevent.joinall(threads)



def threaded(urls):
    threads = []
    images = []
    for url in urls:
        t = urlFetcher(url)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    for t in threads:
        print "image " + str(len(t.images))
        for image in t.images:
            images.append(image)
    print "got the images " + str(len(images))


urls = ['http://www.fubiz.net/?s=car&type=posts',
        'http://www.fubiz.net/?s=lady&type=posts',
        'http://www.fubiz.net/?s=2013&type=posts',
        'http://www.fubiz.net/?s=ball&type=posts']


threadLock = threading.Lock()

if sys.argv[1] == 'a':
    print('Asynchronous:')
    a = datetime.now()
    asynchronous(urls)
    b = datetime.now()
    print b - a

elif sys.argv[1] == 't':
    print('Threaded:')
    a = datetime.now()
    threaded(urls)
    b = datetime.now()
    print b - a
else:
    print('Synchronous:')
    a = datetime.now()
    synchronous(urls)
    b = datetime.now()
    print b - a


