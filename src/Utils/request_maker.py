import os
import requests
from fake_useragent import UserAgent


NINTENDO_SWITCH_WIKI_URL = "https://reddit.com/r/nintendoswitch/wiki/games"
TEST_DATA_DIR = "./test_data"
TEST_DATA_FILE = TEST_DATA_DIR+"/test_data.html"

def get_text_body_from_url(url):
    ua = UserAgent()
    headers = {
         'User-Agent': ua.random
    }
    r = requests.get(url, headers=headers)
    return r.text

def get_test_file():
    if os.path.isdir(TEST_DATA_DIR):
        file = open(TEST_DATA_FILE,"r",encoding='utf-8')
        text = file.read()
        file.close()
        return text
    else:
        os.mkdir(TEST_DATA_DIR)
        file = open(TEST_DATA_FILE,"w",encoding='utf-8')
        text = get_text_body_from_url(NINTENDO_SWITCH_WIKI_URL)
        file.write(text)
        file.close()
        return text
