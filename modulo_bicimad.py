# CLASE URLEMT.

import requests
import zipfile
import io
class UrlEMT:

    emt = 'https://opendata.emtmadrid.es/'
    general = '/Datos-estaticos/Datos-generales-(1)'

    def __init__(self, valid_url):
        self.__valid_url: set = valid_url
        self.get_links(self.emt, self.general)

    @property # GETTER
    def get_valid_url(self):
        return self.__valid_url

    @property # SETTER
    def set_valid_url(self, new__valid_url):
        self.__valid_url = new__valid_url

    @staticmethod
    def select_valid_urls(link_base, link_grl):
        r = requests.get(f'{link_base}{link_grl}')
        if r.status_code != 200:
            raise ConnectionError('Request to server failed!')
        else:
            bytes = io.BytesIO(r.content)
            #lista_zipfile = zipfile.ZipFile(bytes)
            pass

    def get_links(self, link_base, link_grl):
        pass


UrlEMT.select_valid_urls(UrlEMT.emt, UrlEMT.general)

