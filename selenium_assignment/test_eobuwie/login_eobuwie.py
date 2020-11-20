import time
import json
with open('../config.json', 'r') as file:
    config = json.load(file)


def login_to_eobuwie(driver):
    # go to the site
    driver.get("https://www.eobuwie.com.pl/")

    # close gdpr pop-up
    driver.find_element_by_xpath('//*[@id="top"]/body/div[6]/div/div/div/section/button[2]').click()

    # click on login button
    driver.find_element_by_xpath('//*[@id="top"]/body/header/div[3]/div/div/div[2]/div/a[7]').click()
    time.sleep(5)

    # submit credentials
    driver.find_element_by_xpath('//*[@id="login[username]"]').send_keys(config['email'])
    driver.find_element_by_xpath('//*[@id="login[password]"]').send_keys(config['password'])
    driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/button').click()
