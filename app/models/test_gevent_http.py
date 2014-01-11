from geventhttpclient import HTTPClient
from geventhttpclient.url import URL
import geventhttpclient.httplib
geventhttpclient.httplib.patch()
import httplib2
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import gevent




# def fetch(url,get_headers):
#     url = URL(url)
#     http = HTTPClient(url.host,headers=get_headers)
#     # issue a get request
#     response = http.get(url.path)
#     # read status_code
#     response.status_code
#     # read response body
#     content = response.read()
#     # close connections
#     http.close()
#     return content

def fetch(url,get_headers):
    resp, content = httplib2.Http().request(url,"GET",headers= get_headers)
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



urls = ['http://www.fubiz.net/?s=car&type=posts',
        'http://www.fubiz.net/?s=lady&type=posts',
        'http://www.fubiz.net/?s=2013&type=posts',
        'http://www.fubiz.net/?s=ball&type=posts']

if sys.argv[1] == 'a':
    print('Asynchronous GH :')
    a = datetime.now()
    asynchronous(urls)
    b = datetime.now()
    print b - a
else:
    print('Synchronous GH :')
    a = datetime.now()
    synchronous(urls)
    b = datetime.now()
    print b - a


