from selenium import webdriver
from config import NAME_OF_FILE

def make_screen(url):
    DRIVER = r'geckodriver'
    driver = webdriver.Firefox(executable_path=DRIVER)
    driver.get(url)
    element = driver.find_element_by_tag_name('body')
    element_png = element.screenshot_as_png
    with open(NAME_OF_FILE, "wb") as file:
        file.write(element_png)
    driver.quit()
