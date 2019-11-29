from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json,time
from tkinter import Tk
import pyautogui
import selenium.webdriver.support.ui as ui


#替换为自己的url 并且先运行cookies.py获取cookies

url = 'https://blog.csdn.net/qq_30600259'
driver = webdriver.Chrome()
driver.get(url)

driver.delete_all_cookies()
f1 = open('cookie.txt')
cookie = json.loads(f1.read()) #有人说最好用load读文件 我也不知道为啥
f1.close()







for c in cookie:
    if 'expiry' in c:
        del c['expiry']
    print(c)    
    driver.add_cookie(c)
driver.refresh()



#a=deriver.find_elements_by_class_name('article-item-box csdn-tracking-statistics')
input()
content = driver.find_elements_by_xpath("//div/h4/a[@target='_blank']")
print(content)
weblist = []
for test in content:
    print(test.get_attribute('href')[-9:])
    weblist.append(test.get_attribute('href')[-9:])

'''
#second page  //*[@id="Paging_07021176447662405"]/ul/li[5]
nextpage = driver.find_element_by_xpath('//ul/li[5]')
webdriver.ActionChains(driver).move_to_element(nextpage).click(nextpage).perform()
content = driver.find_elements_by_xpath("//div/h4/a[@target='_blank']")
print(content)
for test in content:
    print(test.get_attribute('href')[-9:])
    weblist.append(test.get_attribute('href')[-9:])
'''







print(weblist)
for test in weblist:
    #driver.get(test)
    driver.execute_script('window.open("https://mp.csdn.net/mdeditor/%s#");' % (test))
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    
    daochu = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/nav/div[2]/div/div[18]/button')
    webdriver.ActionChains(driver).move_to_element(daochu).click(daochu).perform()
    time.sleep(2)
    down = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div/div[2]/div/a[1]/div[2]/div')
    webdriver.ActionChains(driver).move_to_element(down).click(down).perform()
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])





'''
#使用execute打开页面
for test in weblist:
    #driver.get(test)
    driver.execute_script('window.open("%s");' % (test))
    time.sleep(9)
    editor = driver.find_element_by_xpath('//*[@id="mainBox"]/main/div[1]/div[1]/div/div[2]/div[2]/a')
    webdriver.ActionChains(driver).move_to_element(editor).click(editor).perform()
    time.sleep(3)
    daochu = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/nav/div[2]/div/div[18]/button')
    webdriver.ActionChains(driver).move_to_element(daochu).click(daochu).perform()
    time.sleep(2)
    down = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div/div[2]/div/a[1]/div[2]/div')
    webdriver.ActionChains(driver).move_to_element(down).click(down).perform()
    time.sleep(2)
'''



'''
for test in content:
    #print(test.get_attribute('href'))
    tempurl = test.get_attribute('href')
    #print(type(tempurl))                     
    driver.get(tempurl)
    time.sleep(5)
    editor = driver.find_element_by_xpath('//*[@id="mainBox"]/main/div[1]/div[1]/div/div[2]/div[2]/a')
    webdriver.ActionChains(driver).move_to_element(editor).click(editor).perform()
    daochu = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/nav/div[2]/div/div[18]/button')
    webdriver.ActionChains(driver).move_to_element(daochu).click(daochu).perform()
    down = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div/div[2]/div/a[1]/div[2]/div')
    webdriver.ActionChains(driver).move_to_element(down).click(down).perform()
'''