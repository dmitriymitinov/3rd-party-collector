from pyquery import PyQuery
from urllib import request
import logging
import json
import re

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

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

    def grabInfo(self, pattern=None):
        pq = PyQuery(self.connect_to_url())
        try:
            if pattern == None:
                version_str = pq(self.version)
                date_str = pq(self.releaseDate)
                return {'Version': version_str.html(), 'Date': date_str.html()}
            else:
                version_str = pq(self.version).html()
                date_str = pq(self.releaseDate).html()
                clear_version = re.search(pattern, version_str).group(0)
                clear_date = re.search(pattern, date_str).group(0)
                return {'Version': clear_version, 'Date': clear_date}
        except Exception:
            logging.warning('Can\'t find specified selector(s)')

    def getDownloadLink(self, selector, selector2=None):
        pq = PyQuery(self.connect_to_url())
        try:
            if selector2 == None:
                download_link = pq(selector).html()
                return download_link.attr('href')
            else:
                download_link = pq(selector)
                download_link2 = pq(selector2)
                return [download_link.attr('href'), download_link2.attr('href')]
        except Exception:
            logging.warning('Can no access required links')

    def getMozillaLink(self, selector):
        pq = PyQuery(self.connect_to_url())
        try:
            download_linkEnGB86 = pq(selector).html().attr('href')
            # need to add other languages links after testing
        except Exception:
            logging.warning('Can no access required links')

    def isVersionValid(self, pattern=None):
        product_name = self.name
        existing_version = None
        needed_valuese = self.grabInfo(pattern=pattern)
        needed_version = needed_valuese.get('Version')
        try:
            with open('Existing_Versions.json') as file:
                json_data = json.load(file)
            for name, cur_version in json_data.items():
                if product_name == self.name:
                    existing_version = cur_version
                    break
                else:
                    continue
            if existing_version != needed_version:
                return True
            else:
                return False
        except Exception:
            logging.warning('Cant fine name of the product')