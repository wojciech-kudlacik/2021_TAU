# hack for importing methods from different packages
# if you're using pycharm - don't mind the unresolved reference error
# IT. WILL. WORK.
import sys, os
import time
sys.path.insert(0, os.path.abspath('..'))

import json
with open('../config.json', 'r') as file:
    config = json.load(file)

from drivers_package.drivers import choose_driver
from login_eobuwie import login_to_eobuwie as login
from logging_package.logger import create_logfile
from logging_package.logger import create_log
from helper_methods.helper_methods import wait_by_xpath

from selenium.webdriver.common.keys import Keys

# required for logs to be appended to a file
create_logfile()

driver = choose_driver()

login(driver)

# hack for chrome - the searchbar was not being loaded in time
if config['driver'] == 'chrome':
    time.sleep(5)

# search for black shoes
driver.find_element_by_xpath('//*[@id="top"]/body/header/div[4]/div[1]/form/input').send_keys("buty czarne")
driver.find_element_by_xpath('//*[@id="top"]/body/header/div[4]/div[1]/form/input').send_keys(Keys.ENTER)

# click on the first result
try:
    wait_by_xpath(driver, 10, '//*[@id="top"]/body/div[3]/div/div[4]/ul/li[1]/div/a/img')
finally:
    driver.find_element_by_xpath('//*[@id="top"]/body/div[3]/div/div[4]/ul/li[1]/div/a/img').click()

# add to cart
try:
    wait_by_xpath(driver, 10, '//*[@id="product_addtocart_form"]/section/div[2]/div/div[6]/div[3]/div/button')
finally:
    driver.find_element_by_xpath('//*[@id="product_addtocart_form"]/section/div[2]/div/div[6]/div[3]/div/button').click()

# hack for firefox - 'shoe size picker' was being loaded two times and obscured the 'go to cart' element
if config['driver'] == 'firefox':
    time.sleep(5)

# choose size
try:
    wait_by_xpath(driver, 5, '//*[@id="product_addtocart_form"]/section/div[2]/div/div[6]/div[2]/div[1]/div/div/div[1]/div[2]/button[3]')
finally:
    driver.find_element_by_xpath('//*[@id="product_addtocart_form"]/section/div[2]/div/div[6]/div[2]/div[1]/div/div/div[1]/div[2]/button[3]').click()

# go to the shopping cart
try:
    wait_by_xpath(driver, 10, '//*[@id="product_addtocart_form"]/section/div[2]/div/div[6]/div[3]/div/div/div/div/div/div[2]/a')
finally:
    driver.find_element_by_xpath('//*[@id="product_addtocart_form"]/section/div[2]/div/div[6]/div[3]/div/div/div/div/div/div[2]/a').click()

# check if shoes are in the shopping cart and remove them
try:
    wait_by_xpath(driver, 10, '//*[@id="top"]/body/div[3]/div/form/div/div/div/div[2]/h2/a/div[1]')
finally:
    driver.find_element_by_xpath('//*[@id="top"]/body/div[3]/div/form/div/div/div/div[4]/a').click()
    create_log(20, "test finished successfully")

driver.quit()

