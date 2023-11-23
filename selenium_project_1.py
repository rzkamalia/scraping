from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

chrome_options = Options()
# chrome_options.add_argument("--headless") # run in background, so there is no chrome pop up

website = "https://www.audible.com/search"
driver = webdriver.Chrome(options = chrome_options)
driver.get(website)

time.sleep(1)

# pagination
pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.XPATH, './/li')
# last_page = pages[-2].text # can not get the result = 25 from this, so i write manual
last_page = 25

current_page = 1
book_title = []
book_author = []

while current_page <= last_page:
    time.sleep(2)

    container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container ')

    for product in container.find_elements(By.XPATH, './/ul/li[contains(@class, "productListItem")]'):
        book_title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)

    current_page = current_page + 1

    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

driver.quit() # for close chrome

df = pd.DataFrame({'title': book_title, 'author': book_author})
df.to_csv(f'books_pagination.csv', index = False)
print(f'process done, books_pagination.csv created')