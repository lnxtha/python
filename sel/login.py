from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://login.metafilter.com')

a = browser.find_elements_by_tag_name('a')

for i in a:
	print(i.text)

username = browser.find_element_by_id('user_name')
password = browser.find_element_by_id('user_pass')

input_password =input('Input Password')

username.send_keys('linusxrstha@gmail.com')
password.send_keys(input_password)
password.submit()

