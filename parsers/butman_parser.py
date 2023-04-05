from .utils import Parser


class ButmanParser(Parser):

    url = 'https://moscow.butmanclub.ru/'

    @classmethod
    def get_name_and_time(cls):
        try:
            return cls.get_soup().find('div', attrs={'class': 't778__title t-name t-name_md js-product-name'}).text
        except Exception as error:
            return cls.NO

    @classmethod
    def get_about(cls):
        try:
            return cls.get_soup().find('div', attrs={'class': 't778__descr t-descr t-descr_xxs'}).text
        except Exception:
            return cls.NO
