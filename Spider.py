from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests

class Spider:
    """
    Класс для полученипя данных из сайта по url
    """

    def __init__(self, url): # предварительная подготовка
        self.url = url
        ua = UserAgent()
        self.agent = {'User-agent': ua.firefox}
        res = requests.get(url, headers=self.agent).text
        self.soup = BeautifulSoup(res, 'lxml')

    def get_status(self):
        '''

        :return: [status code] :int
        '''
        r = requests.get(self.url, headers=self.agent)
        return int(r.status_code)

    def get_html(self): # возвразщает обьект супа
        return self.soup

def safe_image(src):
    p = requests.get(src)
    out = open("img.jpg", "wb")
    out.write(p.content)
    out.close()

safe_image('https://yandex.ru/images/search?p=19&text=%D1%86%D0%B2%D0%B5%D1%82%D1%8B&pos=791&rpt=simage&img_url=https%3A%2F%2Flook.com.ua%2Fpic%2F201210%2F1920x1200%2Flook.com.ua-48596.jpg')