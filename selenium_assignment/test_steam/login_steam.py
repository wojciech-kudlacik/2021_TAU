import json
with open('../config.json', 'r') as file:
    config = json.load(file)


def login_to_steam(driver):

    # go to the site
    driver.get("https://store.steampowered.com/")

    # click on the login button
    driver.find_element_by_xpath('//*[@id="global_action_menu"]/a').click()

    # submit credentials
    driver.find_element_by_id("input_username").send_keys(config['username'])
    driver.find_element_by_id("input_password").send_keys(config['password'])
    driver.find_element_by_xpath('//*[@id="login_btn_signin"]/button').click()