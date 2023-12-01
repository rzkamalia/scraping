# scaping single page

import requests
from bs4 import BeautifulSoup

website = "https://subslikescript.com/movie/Interstellar-816692"

# fetch website
result = requests.get(website)
# get the content
content = result.text

soup = BeautifulSoup(content, "lxml")
box = soup.find('article', class_ = "main-article")
title = box.find('h1').get_text()
transcript = box.find('div', class_ = "full-script").get_text(strip = True, separator = ' ')

with open(f'bs-{title}.txt', 'w') as file:
    file.write(transcript)