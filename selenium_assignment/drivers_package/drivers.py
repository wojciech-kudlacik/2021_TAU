from selenium import webdriver

import json
with open('../config.json', 'r') as file:
    config = json.load(file)


def choose_driver():
    driver_type = config['driver']
    if driver_type == "chrome":
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver
    elif driver_type == "firefox":
        return webdriver.Firefox()
    elif driver_type == "opera":
        return webdriver.Opera()
