

# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options)

import json
with open('../config.json', 'r') as file:
    config = json.load(file)


def login_to_steam(driver):

    driver.get("https://store.steampowered.com/")
    driver.find_element_by_xpath('//*[@id="global_action_menu"]/a').click()
    driver.find_element_by_id("input_username").send_keys(config['username'])
    driver.find_element_by_id("input_password").send_keys(config['password'])
    driver.find_element_by_xpath('//*[@id="login_btn_signin"]/button').click()