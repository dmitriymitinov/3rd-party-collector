from pyquery import PyQuery
from urllib import request
import logging

logging.basicConfig(filename='log.txt',level=logging.DEBUG)

class Product:
    def __init__(self, name, url, version_tag, releseDate_tag):
        self.name = name
        self.url = url
        self.version = version_tag
        self.releaseDate = releseDate_tag

    def connect_to_url(self):
        try:
            response = request.urlopen(self.url)
            html = response.read()
            return html
        except Exception:
            logging.warning('Can not connect to url')

    def grabInfo(self):
        pq = PyQuery(self.connect_to_url())
        try:
            version_str = pq(self.version)
            date_str = pq(self.releaseDate)
        except Exception:
            logging.warning('Can\'t find specified selector')

    def getDownloadLink(self, selector):
        pq = PyQuery(self.connect_to_url())

        download_link = pq(selector)