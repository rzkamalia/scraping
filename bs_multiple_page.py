# scaping multiple page

import requests
from bs4 import BeautifulSoup

root = "https://subslikescript.com/"
website = root + "movies"

# fetch website
result = requests.get(website)
# get the content
content = result.text

soup = BeautifulSoup(content, "lxml")
box = soup.find('article', class_ = "main-article")
links = []
for link in box.find_all('a', href = True):
    # get the link 
    link = link["href"]
    link = root + link

    result_1 = requests.get(link)
    content_1 = result_1.text
    soup_1 = BeautifulSoup(content_1, "lxml")

    box_1 = soup_1.find('article', class_ = "main-article")
    title = box_1.find('h1').get_text()
    transcript = box_1.find('div', class_ = "full-script").get_text(strip = True, separator = ' ')

    with open(f'{title}.txt', 'w') as file:
        file.write(transcript)