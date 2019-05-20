from selenium.webdriver import Chrome
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = Chrome()

wait = WebDriverWait(browser, 20)

URL = 'buketlab.com/kontakty/'

browser.get('https://' + URL)
form = browser.find_element_by_css_selector('form[name="darvin_feedback_order"]')
inputs = form.find_elements_by_css_selector('input[required = "required"]')

# print(inputs)
for field in inputs:
    if field.get_attribute('id') == 'darvin_feedback_order_name':
        field.send_keys('Иван')
    elif field.get_attribute('id') == 'darvin_feedback_order_phone':
        field.send_keys('9205686965')
    else:
        print('Не опознанное поле')
        browser.close()

form.submit()

try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'success-form')))
    success = browser.find_element_by_class_name('success-form')
    assert success.find_element_by_tag_name('h1').text == 'Ваш заказ успешно отправлен!', 'Форма не отправилась'
    browser.close()

except NoSuchElementException as e:
    print('Ошибка поиска элемента {}'.format(e))
    browser.close()

# assert success
