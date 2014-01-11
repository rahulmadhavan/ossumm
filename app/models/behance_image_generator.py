from httplib2 import Http
from bs4 import BeautifulSoup
from image import Image

class BehanceImageGenerator:

    SOURCE_NAME = 'Behance'
    SOURCE_ROOT = 'http://www.behance.net/'
    search_url = 'http://www.behance.net/search?search={0}'

    def generate_images(self,arguments = {}):
        resp, content = Http().request(self.search_url.format(arguments['search_term']),"GET",headers = arguments['headers'])
        return self.parse_content(content,arguments)

    def parse_content(self,content,arguments):
        soup = BeautifulSoup(content,"lxml")
        images = []
        for div in soup.find_all('div',attrs={'class':'covers'}):
            for img in div.find_all('img'):
                aurl = img.parent.parent.attrs.get('href',"")
                url = img.attrs.get('src',"")
                alt = img.attrs.get('alt',"")
                images.append(Image(self.SOURCE_NAME,self.SOURCE_ROOT,url,alt,aurl))
        return images


#
# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) '
#                                 'Chrome/31.0.1650.63 Safari/537.36'}
# bhg = BehanceImageGenerator()
# content = bhg.generate_images({'headers':headers, 'search_term':'car'})
# print content