from .utils import Parser


class KozlovParser(Parser):

    url = 'https://kozlovclub.ru/'

    @classmethod
    def get_bit(cls):
        try:
            return cls.get_soup().find('div', attrs={'class': 'today_1'}).find('a', attrs={'class': 'title'}).text
        except Exception as error:
            return cls.NO

    @classmethod
    def get_masnic(cls):
        return cls.get_soup().find_all('div', attrs={'class': 'today_1'})[2].find('a', attrs={'class': 'title'}).text

    @classmethod
    def get_main(cls):
        try:
            return cls.get_soup().find_all('div', attrs={'class': 'today_1'})[1].find('a', attrs={'class': 'title'}).text
        except Exception:
            return cls.NO

    @classmethod
    def get_mansard(cls):
        try:
            return cls.get_soup().find_all('div', attrs={'class': 'today_1'})[3].find('a', attrs={'class': 'title'}).text
        except Exception:
            return cls.NO
