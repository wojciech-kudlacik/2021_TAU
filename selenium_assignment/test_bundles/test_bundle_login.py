import sys, os
sys.path.insert(0, os.path.abspath('..'))

import json
with open('../config.json', 'r') as file:
    config = json.load(file)

from drivers_package.drivers import choose_driver
from test_eobuwie.login_eobuwie import login_to_eobuwie
from test_steam.login_steam import login_to_steam

driver = choose_driver()

login_to_eobuwie(driver)
login_to_steam(driver)

