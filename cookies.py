from selenium import webdriver
import time,json
#替换掉url

url = 'https://blog.csdn.net/xxxx'
driver = webdriver.Chrome()
driver.get(url)
input("登入后输入任意字符")
cookies = driver.get_cookies()
print(cookies)
f1 = open('cookie.txt','w')
f1.write(json.dumps(cookies))
f1.close()