import bs4
from Utils.request_maker import get_test_file
from Utils.scrapper import iterate_table

html = get_test_file()
#response = get_text_body_from_url("https://www.reddit.com/r/NintendoSwitch/wiki/games")
soup = bs4.BeautifulSoup(html, 'html.parser', from_encoding="utf-8")
released_table_body = soup.find("h2",id="wiki_released").findNext('table').findNext("tbody")
iterate_table(released_table_body)
planned_table_body = soup.find("h2",id="wiki_planned").findNext('table').findNext("tbody")
table = iterate_table(planned_table_body)
for i in table:
    print(i)
table = iterate_table(released_table_body)
for i in table:
    print(i)
