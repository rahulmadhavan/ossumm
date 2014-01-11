class Image:

    IMAGE_HTML_TEMPLATE = "<img src={0} alt={1}>"
    ANCHOR_HTML_TEMPLATE = "<a href={0}>{1}</a>"

    def __init__(self,name,root,url,alt,aurl):
        self._name = name
        self._root = root
        self._url = url
        self._alt = alt
        self._aurl = aurl

    def get_html(self):
        image_html = Image.IMAGE_HTML_TEMPLATE.format(self._url.encode('utf-8'),self._alt.encode('utf-8'))
        anchor_html = Image.ANCHOR_HTML_TEMPLATE.format(self._aurl.encode('utf-8'),image_html)
        return anchor_html

    def get_html_for_images(images):
        html = []
        for image in images:
            html.append(image.get_html)
        return ",".join(html)

    def __str__(self):
        return self.get_html()