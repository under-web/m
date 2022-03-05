# from Spider import Spider
#
#
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
list_urls = []
url = 'https://yandex.ru/images/search?text=%D1%86%D0%B2%D0%B5%D1%82%D1%8B&from=tabbar'
#
# obj = Spider(url)
# print(obj.get_status())
# images =  obj.soup.find_all('a')
# for i in images:
#     try:
#         if 'jpg' in i.get('href'):
#             print(i.get('href'))
#     except Exception as e:
#         print(e)




from selenium import webdriver

browser = webdriver.Firefox()

browser.get(url)
# try:
#     html = browser.find_element(By.CLASS_NAME, "websearch-button__text")
#     for i in range(5):
#         html.send_keys(Keys.END)
#         time.sleep(3)
# except Exception as e:
#     print(e)
# finally:
#     browser.close()
#     browser.quit()
time.sleep(3)
for i in range(20):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

button = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/a').click()

for i in range(20):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
try:
    elems = browser.find_elements(By.XPATH, "//a[@href]")
    for elem in elems:
        list_urls.append(elem.get_attribute("href"))
        print(elem.get_attribute("href"))
    print(f' Страница {len(list_urls)} собрано. ')

except Exception as e:
    print('err code 2', e)
finally:
    time.sleep(5)
    browser.close()
    browser.quit()

