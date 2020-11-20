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

from selenium.webdriver.common.keys import Keys

driver = choose_driver()

def test_wishlist_steam(driver):

    # required for logs to be appended to a file
    create_logfile()

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

    # add to wishlist
    try:
        wait_by_xpath(driver, 10, '//*[@id="add_to_wishlist_area"]/a')
    finally:
        driver.find_element_by_xpath('//*[@id="add_to_wishlist_area"]/a').click()
        # go to wishlist
        # hack for opera - loads really slowly
        time.sleep(2)
        driver.find_element_by_id("wishlist_link").click()

    # check if the cyberpunk 2077 is on wishlist
    try:
        wait_by_xpath(driver, 10, '//*[@id="wishlist_ctn"]/div/a')
    finally:
        create_log(20, "cyberpunk is on wishlist")
        driver.find_element_by_xpath('//*[@id="wishlist_ctn"]/div/div[2]/div[2]/div[2]/div[2]/div').click()

    # remove from wishlist
    try:
        wait_by_xpath(driver, 5, '/html/body/div[8]/div[3]/div/div[2]/div[1]')
    finally:
        driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[2]/div[1]').click()
        create_log(20, "test finished successfully")

    driver.quit()

test_wishlist_steam(driver)
