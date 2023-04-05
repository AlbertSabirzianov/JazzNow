from .utils import Parser


class EsseParser(Parser):

    url = 'https://www.jazzesse.ru/'

    @classmethod
    def get_main(cls):
        return cls.get_soup().find_all('div', attrs={'class': 'desc'})[0].find('a').text

    @classmethod
    def get_lab(cls):
        return cls.get_soup().find_all('div', attrs={'class': 'desc'})[1].find('a').text

