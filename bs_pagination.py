import requests
from bs4 import BeautifulSoup

root = "https://subslikescript.com/"
website = root + "movies"

# fetch website
result = requests.get(website)
# get the content
content = result.text

soup = BeautifulSoup(content, "lxml")
pagination = soup.find('ul', class_ = "pagination")
pages = pagination.find_all('li', class_ = "page-item")
last_page = pages[-2].get_text()
for i in range(1, int(last_page) + 1):
    # get the link 
    link = f"{website}?page={i}"

    # fetch link
    result_1 = requests.get(link)
    # get content
    content_1 = result_1.text
    soup_1 = BeautifulSoup(content_1, "lxml")

    box_1 = soup_1.find('article', class_ = "main-article")
    script_list = box_1.find('ul', class_ = "scripts-list")
    for movie_link in script_list.find_all('a', href = True):
        # get the link of each movie
        movie_link = movie_link["href"]
        movie_link = root + movie_link

        try:
            # fetch movie link
            result_2 = requests.get(movie_link)
            # get the content
            content_2 = result_2.text
            soup_2 = BeautifulSoup(content_2, "lxml")

            box_2 = soup_2.find('article', class_ = "main-article")
            title = box_2.find('h1').get_text()
            transcript = box_2.find('div', class_ = "full-script").get_text(strip = True, separator = ' ')

            with open(f'bs-pagination/{title}.txt', 'w') as file:
                file.write(transcript)
                print(f'bs-pagination/{title}.txt created')
        
        except:
            print(f'{movie_link} not works')