from selenium import webdriver
from os.path import dirname, abspath

# getting chromedriver path using the project root directory
project_root = dirname(dirname(abspath(__file__)))
chromedriver_path = "chromedriver.exe"

# test URL
url = "https://www.seleniumhq.org/"
# expected page title
expected_page_title = "Selenium - Web Browser Automation"

driver = webdriver.Chrome(chromedriver_path)
driver.get(url)

try:
    assert expected_page_title == driver.title
    print("Success: Page title matches the expected title i.e.", expected_page_title)
except (AssertionError):
    print("Error: Page title does not match the expected title")
finally:
    driver.quit()