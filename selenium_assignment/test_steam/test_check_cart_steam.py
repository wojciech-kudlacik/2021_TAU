# hack for importing methods from different packages
# if you're using pycharm - don't mind the unresolved reference error
# IT. WILL. WORK.
import sys, os
import time

sys.path.insert(0, os.path.abspath('..'))
from drivers_package.drivers import choose_driver
from login_steam import login_to_steam as login
from logging_package.logger import create_logfile
from logging_package.logger import create_log
from helper_methods.helper_methods import wait_by_xpath
from helper_methods.helper_methods import wait_by_class

from selenium.webdriver.common.keys import Keys

# required for logs to be appended to a file
create_logfile()

driver = choose_driver()

# login
login(driver)

# search for cyberpunk 2077
try:
    wait_by_xpath(driver, 10, '//*[@id="store_nav_search_term"]')
finally:
    driver.find_element_by_xpath('//*[@id="store_nav_search_term"]').send_keys("cyberpunk 2077")
    driver.find_element_by_xpath('//*[@id="store_nav_search_term"]').send_keys(Keys.ENTER)

# choose cyberpunk 2077 from the list
try:
    element = wait_by_xpath(driver, 10, '/html/body/div[1]/div[7]/div[4]/form/div[1]/div/div[1]/div[3]/div/div[3]/a[1]/div[1]/img')
finally:
    # hack for firefox - the element does not execute with a normal .click()
    driver.execute_script("arguments[0].click();", element)

# add to cart
try:
    wait_by_xpath(driver, 10, '//*[@id="btn_add_to_cart_367653"]')
finally:
    driver.find_element_by_xpath('//*[@id="btn_add_to_cart_367653"]').click()

# check if cyberpunk is in the cart
try:
    wait_by_class(driver, 10, class_name='cart_item')
finally:
    driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[1]/div[2]/div[4]/div[2]/div/a').click()

# remove from cart
try:
    wait_by_xpath(driver, 5, '/html/body/div[3]/div[3]/div/div[2]/div[1]')
finally:
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[2]/div[1]').click()
    create_log(20, "test finished successfully")

driver.quit()


