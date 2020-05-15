import time
from selenium import webdriver
#driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
browser = webdriver.Firefox()

browser.get('https://inventwithpython.com')


try:
    elem = browser.find_elements_by_css_selector('margin')
    for i in elem:
        print('Found <%s> element with that class name!' % (elem.tag_name))
    
except:
    print('Was not able to find an element with that name.')
