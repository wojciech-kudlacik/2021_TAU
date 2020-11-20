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

driver = choose_driver()



# required for logs to be appended to a file
create_logfile()

login(driver)

# hack for chrome - the searchbar was not being loaded in time
if config['driver'] == 'chrome':
    time.sleep(5)

# search for black shoes
driver.find_element_by_xpath('//*[@id="top"]/body/header/div[4]/div[1]/form/input').send_keys("buty czarne")
driver.find_element_by_xpath('//*[@id="top"]/body/header/div[4]/div[1]/form/input').send_keys(Keys.ENTER)

if config['driver'] == 'firefox':
    time.sleep(5)
# add the first result to favourites
try:
    wait_by_xpath(driver, 10, '//*[@id="top"]/body/div[3]/div/div[4]/ul/li[1]/div/a/img')
finally:
    driver.find_element_by_xpath('//*[@id="top"]/body/div[3]/div/div[4]/ul/li[1]/div/button').click()
    time.sleep(5)
    # go to favourites
    driver.find_element_by_xpath('//*[@id="top"]/body/header/div[3]/div/div/div[2]/div/a[5]').click()

# delete from favourites
try:
    wait_by_xpath(driver, 10, '//*[@id="top"]/body/div[3]/div/ul/li/div/a/div[1]/img')
finally:
    driver.find_element_by_xpath('//*[@id="top"]/body/div[3]/div/ul/li/div/button').click()

time.sleep(2)
create_log(20, "test finished successfully")

driver.quit()


