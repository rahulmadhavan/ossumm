from httplib2 import Http
from bs4 import BeautifulSoup
from image import Image

class MatboardImageGenerator:

    SOURCE_NAME = 'thematboard'
    SOURCE_ROOT = 'http://thematboard.com'
    search_url = 'http://thematboard.com/actions/get_mats_AJAX.php?cat=&type=search&limit=10&start=1&searchterm={0}'

    def generate_images(self,arguments = {}):
        resp, content = Http().request(self.search_url.format(arguments['search_term']),"GET",headers = arguments['headers'])
        return self.parse_content(content,arguments)

    def parse_content(self,content,arguments):
        soup = BeautifulSoup(content,"lxml")
        images = []
        for div in soup.find_all('div',attrs={'class':'mat'}):
            for img in div.find_all('img'):
                aurl = img.parent.attrs.get('href',"")
                iurl = img.attrs.get('src',"")
                if 'http' in iurl:
                    url = iurl
                else:
                    url = self.SOURCE_ROOT+iurl
                alt = img.attrs.get('alt',"ossumm")
                images.append(Image(self.SOURCE_NAME,self.SOURCE_ROOT,url,alt,aurl))
        return images


# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) '
#                                 'Chrome/31.0.1650.63 Safari/537.36'}
# bhg = MatboardImageGenerator()
# content = bhg.generate_images({'headers':headers, 'search_term':'car'})
# print content

