import requests
from bs4 import BeautifulSoup


class Parser:
    headers = {
        'Accept': '* / *',
        'user-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    }
    NO = 'Что то пошло не так'

    url: str = ''

    @classmethod
    def get_soup(cls):
        html = requests.get(url=cls.url, headers=cls.headers)
        soup = BeautifulSoup(html.text, 'lxml')
        return soup
