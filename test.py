from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


browser = Chrome()
browser.get('https://google.com')
search_string = browser.find_element_by_css_selector('input[name="q"]')
search_string.send_keys('test')
search_string.submit()
# search_string.send_keys(Keys.ENTER)
# button = browser.find_element_by_css_selector('input[name="btnK"]')
# button.click()
