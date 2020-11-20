# hack for importing methods from different packages
# if you're using pycharm - don't mind the unresolved reference error
# IT. WILL. WORK.
import sys, os
import time

sys.path.insert(0, os.path.abspath('..'))
from drivers_package.drivers import choose_driver
from login_eobuwie import login_to_eobuwie as login
from logging_package.logger import create_logfile
from logging_package.logger import create_log
from helper_methods.helper_methods import wait_by_xpath
from helper_methods.helper_methods import wait_by_class

from selenium.webdriver.common.keys import Keys

# required for logs to be appended to a file
# create_logfile()

driver = choose_driver()

login(driver)
