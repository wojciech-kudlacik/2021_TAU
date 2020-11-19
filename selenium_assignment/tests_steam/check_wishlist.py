from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from login_steam import login_to_steam as login


driver = webdriver.Chrome()

# login
login(driver)

# search for cyberpunk 2077
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="store_nav_search_term"]'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="store_nav_search_term"]').send_keys("cyberpunk 2077")
    driver.find_element_by_xpath('//*[@id="store_nav_search_term"]').send_keys(Keys.ENTER)

# choose cyberpunk 2077 from the list
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="search_resultsRows"]/a[1]'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="search_resultsRows"]/a[1]').click()

# add to wishlist
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add_to_wishlist_area"]/a'))
    )
finally:
    driver.find_element_by_xpath('//*[@id="add_to_wishlist_area"]/a').click()
    # go to wishlist
    driver.find_element_by_id("wishlist_link").click()

# check if the cyberpunk 2077 is on wishlist
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="wishlist_ctn"]/div/a'))
    )
finally:
    # TODO log to file
    print('cyberpunk landed')
    driver.find_element_by_xpath('//*[@id="wishlist_ctn"]/div/div[2]/div[2]/div[2]/div[2]/div').click()

# remove from wishlist
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/div[3]/div/div[2]/div[1]'))
    )
finally:
    driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[2]/div[1]').click()
    # TODO log to file
    print('test done')

driver.quit()





