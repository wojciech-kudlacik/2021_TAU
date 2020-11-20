from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def wait_by_xpath(webdriver, time_amount, xpath):
    element_to_return = WebDriverWait(webdriver, time_amount).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return element_to_return


def wait_by_id(webdriver, time_amount, element_id):
    element_to_return = WebDriverWait(webdriver, time_amount).until(
        EC.presence_of_element_located((By.ID, element_id))
    )
    return element_to_return
