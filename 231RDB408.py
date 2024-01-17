import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome()

url = "https://www.salidzini.lv/"
driver.get(url)

search_box = driver.find_element(By.ID, "q")
search_input = input("Ievadiet datora detaļu: ")
search_box.send_keys(search_input)
search_box.send_keys(Keys.RETURN)
time.sleep(10)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
listings = soup.find_all('img', {'src': '//static.salidzini.lv/img/iesaka.png'})

for listing in listings:
    a = listing.find_parent('a')
    if a:
        href = a['href']
        listing_url = url + href
        print(f"URL: {listing_url}")

driver.quit()
