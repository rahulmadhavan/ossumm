import threading
from datetime import datetime
import sys
from behance_image_generator import BehanceImageGenerator
from fubiz_image_generator import FubizImageGenerator
from design_you_trust_image_generator import DesignYouTrustImageGenerator
from matboard_image_generator import MatboardImageGenerator

class ImageFetcher(threading.Thread):

    def __init__(self,generator,arguments):
        threading.Thread.__init__(self)
        self._generator = generator
        self._arguments = arguments
        self._images = []
    def run(self):
        self._images = self._generator.generate_images(self._arguments)

class ImageGenerator:

    def generate(self,search_term):
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/31.0.1650.63 Safari/537.36'}
        generators = [BehanceImageGenerator(),FubizImageGenerator(),DesignYouTrustImageGenerator(),MatboardImageGenerator()]
        image_fetchers = []
        images = []
        for generator in generators:
            image_fetchers.append(ImageFetcher(generator,{'headers':headers, 'search_term':search_term}))
        for image_fetcher in image_fetchers:
            image_fetcher.start()
        for image_fetcher in image_fetchers:
            image_fetcher.join()
        for image_fetcher in image_fetchers:
            for image in image_fetcher._images:
                images.append(image)
        return images

    def generates(self,search_term):
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/31.0.1650.63 Safari/537.36'}
        generators = [BehanceImageGenerator(),FubizImageGenerator(),DesignYouTrustImageGenerator(),MatboardImageGenerator()]
        for generator in generators:
            generator.generate_images({'headers':headers, 'search_term':search_term})


# if sys.argv[1] == 't':
#     print('Threaded:')
#     a = datetime.now()
#     ImageGenerator().generate('car')
#     b = datetime.now()
#     print b - a
# else:
#     print('Synchronous:')
#     a = datetime.now()
#     ImageGenerator().generates('car')
#     b = datetime.now()
#     print b - a


