from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = "https://www.adamchoi.co.uk/overs/detailed"
driver = webdriver.Chrome()
driver.get(website)

time.sleep(1)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event = "All matches"]')
all_matches_button.click() # automate click button All matches when chrome was opened

dropdown = Select(driver.find_element(By.ID, 'country'))
country = 'Spain'
dropdown.select_by_visible_text(country)

time.sleep(3)

matches = driver.find_elements(By.TAG_NAME, 'tr') # 'tr' means //tr

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)
driver.quit() # for close chrome

df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv(f'football_data_{country}.csv', index = False)