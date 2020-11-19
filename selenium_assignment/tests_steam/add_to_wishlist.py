from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from login_steam import login_to_steam as login

import time

# go to steam page
# login
# find gta v
# bypass age restriction
# add to wishlist
# go to wishlist
# remove from wishlist
# driver.quit()

driver = webdriver.Chrome()

# login
login(driver)

# find cyberpunk 2077
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="store_nav_search_term"]'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="store_nav_search_term"]').send_keys("cyberpunk 2077")
    driver.find_element_by_xpath('//*[@id="store_nav_search_term"]').send_keys(Keys.ENTER)

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="search_resultsRows"]/a[1]'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="search_resultsRows"]/a[1]').click()
