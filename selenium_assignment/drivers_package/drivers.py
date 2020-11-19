from selenium import webdriver


def choose_drivers(driver_type):
    if driver_type is "chrome":
        return webdriver.Chrome()
    elif driver_type is "firefox":
        return webdriver.Firefox()
    elif driver_type is "opera":
        return webdriver.Opera()
