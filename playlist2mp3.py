from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

input = input('ENTER A PLAYLIST TO DOWNLOAD: ')
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH) 
driver.get(input)                                                                                                         
time.sleep(1)                                                                                                           

links = []                                                                                                               
def playlist_URLs():
    find_href = driver.find_elements_by_xpath('//*[@id="content"]/a')
    for my_href in find_href:
       links.append((my_href.get_attribute("href")))

playlist_URLs()

driver.get('https://ytmp3.cc/en13/')

failed = ''
correct_tab = driver.current_window_handle

for l in links:
    search = WebDriverWait(driver, 820).until(EC.presence_of_element_located((By.ID, 'input'))).send_keys(l)
    convert = WebDriverWait(driver, 820).until(EC.presence_of_element_located((By.ID, 'submit'))).click()
    time.sleep(2)
    try:
        here = driver.find_element_by_xpath('//*[@id="error"]/p[2]/a[1]')
        here.click()
        time.sleep(2)
        failed = True
    except NoSuchElementException:
        pass
    if failed == True:
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(l)
        actions.send_keys(u'\ue007')
        actions.perform()
        print('CRISIS AVERTED')
    failed = False
    download = WebDriverWait(driver, 820).until(EC.presence_of_element_located((By.LINK_TEXT, 'Download'))).click()
    convertNext = WebDriverWait(driver, 820).until(EC.presence_of_element_located((By.LINK_TEXT, 'Convert next'))).click()
    time.sleep(1)
    driver.switch_to_window(driver.window_handles[0])
    print(str(l) + ' has been downloaded')



print('ALL DOWNLOADS COMPLETE')