#INSTALL SELENIUM BEFORE RUNNING THIS CODE
#pip3 install selenium
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import getpass

#IF USING A RASPBERRY PI, FIRST INSTALL THIS OPTIMIZED CHROME DRIVER
#sudo apt-get install chromium-chromedriver
browser_driver = Service('/usr/lib/chromium-browser/chromedriver')
page_to_scrape = webdriver.Chrome(service=browser_driver)
page_to_scrape.get("https://bannatyne-services.brightlime.com/login/")


username = page_to_scrape.find_element(By.ID, "UserName")
password = page_to_scrape.find_element(By.ID, "Password")
my_username = (input('Enter your username: '))
username.send_keys(my_username)
my_pass = getpass.getpass()
password.send_keys(my_pass)

page_to_scrape.find_element(By.CLASS_NAME, "form-actions").click()

page_to_scrape.get("https://bannatyne-services.brightlime.com/bookings/activities/")

"""
quotes = page_to_scrape.find_elements(By.CLASS_NAME, "text")
authors = page_to_scrape.find_elements(By.CLASS_NAME, "author")

file = open("scraped_quotes2.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])
file.close()
"""

