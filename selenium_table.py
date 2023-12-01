from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

website = "https://www.adamchoi.co.uk/overs/detailed"
driver = webdriver.Chrome()
driver.get(website)

time.sleep(3)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event = "All matches"]')
all_matches_button.click() # automate click button All matches when chrome was opened

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
df.to_csv('selenium_football_data.csv', index = False)