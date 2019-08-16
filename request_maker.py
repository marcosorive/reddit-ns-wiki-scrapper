import requests
from fake_useragent import UserAgent


def get_text_body_from_url(url):
    ua = UserAgent()
    headers = {
         'User-Agent': ua.random
    }
    r = requests.get(url, headers=headers)
    return r.text

def get_test_file():
    file = open("test_data.html","r",encoding='utf-8')
    text = file.read()
    file.close()
    return text
