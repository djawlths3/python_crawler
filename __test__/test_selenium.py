from selenium import webdriver

wd = webdriver.Chrome('D:\cafe24\chromedriver\chromedriver.exe')
wd.get('http://www.google.com')
html = wd.page_source
print(html)
wd.quit()