# Scraping

### Beautiful Soup
+ No JavaScript support.

To run beautiful soup script :
```
$ python3 bs_multiple_page.py
```

### Selenium
+ Actually **not web scraping**. It is web driver designed to render web pages for test automation web apps. 
+ Works with JavaScript.
+ Slower than http requests because all script on web page will be execute.
+ Will be good for small projects.
+ Recommended using Chrome.
+ Problem scraping JavaScript is data loaded dynamically, so it cn take some second to load completely. So we need to add wait function. There are two wait functions, namely as follows.
1. **Implicit wait** is used to tell web driver to wait for a certain time. Code :
```
import time

time.sleep(n) # n in second
```
2. **Explicit wait** is used to tell web driver wait for spesific condition to occur. Code :
```
from selenium.webdriver.support.ui import WebDriverWait

WebDriverWait(driver, 10).until(...) # if after 10 second condition is not satisfied, the code is going to break.
```
**Recommendation using explicit wait, cause program will execute next script as soon as condition is satisfied.**

### Scrapy
+ Will be href for large projects where speed is priority.
+ Used command :
```
1. genspider — generate new spider using pre-defined templates.
2. startproject — create new project.
3. shell — trying the code. 
```

To generate scrapy spider:
```
1. $ scrapy startproject project_name
2. $ cd project_name/project_name
3. $ scrapy genspider python_scipt_name url_website
```
To running scrapy:
```
$ scrapy crawl python_scipt_name
```
If you want directly save the result to csv:
```
$ scrapy crawl python_scipt_name -o filename.csv
```
**If project folder already exists, you can simply running scrapy. Make sure you inside project_name/project_name.**

### Note 
To check website works with JavaScript :
```
1. Click right.
2. Click "Inspect (Q)".
3. Click "...".
4. To Advanced settings, then checklist "Disable JavaScript".
5. Then reload the website. If error or keep loading or does not display anything, thats mean its works with JavaScript. 
```
