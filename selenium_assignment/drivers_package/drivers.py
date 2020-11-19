from selenium import webdriver

import json
with open('../config.json', 'r') as file:
    config = json.load(file)


def choose_driver():
    driver_type = config['driver']
    if driver_type == "chrome":
        return webdriver.Chrome()
    elif driver_type == "firefox":
        return webdriver.Firefox()
    elif driver_type == "opera":
        return webdriver.Opera()
