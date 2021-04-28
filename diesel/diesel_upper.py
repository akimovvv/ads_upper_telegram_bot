import random
import time
from selenium.webdriver.common.keys import Keys

user_ads_links = []


def upper(text, browser):
    for i in user_ads_links:
        time.sleep(random.randrange(3, 8))
        browser.get(i)
        time.sleep(5)
        input_place = browser.find_element_by_xpath('/html/body/div[1]/div[5]/div[7]/div[3]/div/div[1]/form/span/span[2]/span/table/tbody/tr[2]/td/iframe')
        input_place.send_keys(text)
        time.sleep(random.randrange(3, 8))
        submit_but = browser.find_element_by_xpath('/html/body/div[1]/div[5]/div[7]/div[3]/div/div[1]/form/fieldset/input[1]')
        submit_but.click()
        time.sleep(10)
        print('Объявление поднято...')
    browser.close()
    browser.quit()


def count_ads_user(browser):
    time.sleep(random.randrange(3, 8))
    browser.find_element_by_id("user_link").click()
    time.sleep(random.randrange(3, 7))
    browser.find_element_by_id("user_content").click()
    time.sleep(random.randrange(3, 8))
    hrefs = browser.find_elements_by_tag_name("a")
    print('Сбор Ссылок...')

    for item in hrefs:
        value = item.get_attribute("href")
        if str(value).endswith('&hl='):
            user_ads_links.append(value)
            print('Вставляем в список...')

def sing_in(username, password, browser):
    browser.get('https://diesel.elcat.kg/')
    time.sleep(5)
    browser.find_element_by_id('sign_in').click()
    time.sleep(random.randrange(2, 10))
    input_username = browser.find_element_by_name('ips_username')
    input_username.clear()
    input_username.send_keys(username)
    time.sleep(random.randrange(2, 10))
    input_password = browser.find_element_by_name('ips_password')
    input_password.clear()
    input_password.send_keys(password)
    input_password.send_keys(Keys.ENTER)
    print('Вошёл в аккаунт...')

def sing_in_check(browser):
    try:
        if browser.find_element_by_id("user_link").is_displayed():
            return True
        else:
            return False
    except Exception as ex:
        print(ex)
