"""This is a basic webscraper to retrieve a list of Russian surnames from a wikipedia page.

Typical Usage:
        ws = WebScraper()
        surnames = ws.get_surnames()
        print(surnames)
"""

from bs4 import BeautifulSoup
import requests


class WebScraper:
    def __init__(self):
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/54.0.2840.71 Safari/537.36'
        }
        self.soup = BeautifulSoup()
        self.wikipedia_russian_surnames = "https://en.wikipedia.org/wiki/List_of_surnames_in_Russia"

    def make_soup(self, file_name):
        with open(file_name, "r", encoding="UTF-8") as f:
            soup_ = BeautifulSoup(f, 'html.parser')
        return soup_

    def get_surnames(self):
        session = requests.session()
        response = session.get(self.wikipedia_russian_surnames, headers=self.headers)
        soup = BeautifulSoup(response.text, features="html.parser")
        out = []
        for i in soup.findAll('span', style='font-size:85%;'):
            out.append(str(i).split('(')[1].split(')')[0])
        return out
