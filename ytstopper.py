import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--disable-sync')
driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

print('Enter youtube url : ')
url = input()

driver.get(url)
video = driver.find_element_by_id('ytd-player')

