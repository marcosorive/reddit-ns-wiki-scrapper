import bs4
from request_maker import get_text_body_from_url, get_test_file
from Game import Game
import re

def get_name_link(element):
    anchor = element.find("a")
    if anchor:
        name = element.find("a").text
        link = element.find("a").attrs["href"]
    else:
        name = element.text
        link = ""
    return name, link
    
def get_dev_pub(input):
    splitted = input.text.split("/")
    if len(splitted) == 1:
        dev = publisher = splitted[0]
    else:
        dev = splitted[0]
        publisher = splitted[1]
    return dev, publisher

def get_dates(input):
    dates = input.text
    result = dict()
    '''
    Date types:
        January 3, 2019 (NA), December 27, 2018 (EU), September 6, 2018 (JP)
        Spring 2019/Early 2019/April 2019
        TBD
    '''
    one_date_pattern = r"(\w+ \d+, \d+)"
    multiple_date_pattern =  r"(\w+ \d+, \d+ )(\(\w+\)|\(\w+, \w+\))"
    season_year_pattern = r"(\w+) (\d+)"
    if re.match(multiple_date_pattern,dates):
        dates = re.findall(multiple_date_pattern,dates)
        for regional_date in dates:
            result[regional_date[1].strip("(").strip(")")] = regional_date[0].rstrip().lstrip()
    elif re.match(one_date_pattern,dates):
        result["ALL"] = re.findall(one_date_pattern,dates)[0]
    elif re.match(season_year_pattern,dates):
        result["ALL"] = re.findall(season_year_pattern,dates)[0][1]
    else:
        result["ALL"] = "TBD"

    return result

def get_trailer_link(element):
    if element.find("a"):
        return element.find("a").attrs["href"] or ""
    return ""

'''Function that given a <tr> elements extracts the data of the game.

Parameters:
    row (bs4.element.Tag): a <tr> element.

Returns:

'''
def get_data_from_table_row(row):
    row_data = list(filter(lambda x: x!="\n" , row.contents))
    if len(row_data) != 4:
        return None
    game = Game()
    game.name, game.link = get_name_link(row_data[0])
    game.dev, game.publisher = get_dev_pub(row_data[1])
    game.dates = get_dates(row_data[2])
    game.trailer_link = get_trailer_link(row_data[3])
    return game
    

'''Function that iterates every row in a table.

'''
def iterate_table(table):
    all_games = list()
    for child in table.children:
        if isinstance(child, bs4.element.Tag):
            all_games.append(get_data_from_table_row(child))
    return all_games


html = get_test_file()
#response = get_text_body_from_url("https://www.reddit.com/r/NintendoSwitch/wiki/games")
soup = bs4.BeautifulSoup(html, 'html.parser', from_encoding="utf-8")
released_table_body = soup.find("h2",id="wiki_released").findNext('table').findNext("tbody")
iterate_table(released_table_body)