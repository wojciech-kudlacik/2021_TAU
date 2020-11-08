from selenium import webdriver
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Opera()
driver.get("https://www.nytimes.com")
headlines = driver.find_elements_by_class_name("story-heading")
for headline in headlines:
    print(headline.text.strip()
