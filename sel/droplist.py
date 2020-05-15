import time

from selenium import webdriver  # import selenium driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  #import keys
from selenium.common.exceptions import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from getpass import getpass

file = open("droplist.txt","r")
#print(file.read())

description = ' Please drop following schemas:\n'+file.read()
print(description)

username = 'i213117'
password = getpass('Password:\n')
#description = ' Please drop following schemas:\nOE0667001SUNIL1\nOE0819001200300'

driver = webdriver.Firefox()

# base login
driver.get("https://jira2.cotiviti.com/secure/Dashboard.jspa") # get URL
time.sleep(5)


# Logging in
try:
	login_email = driver.find_element_by_id('login-form-username').send_keys(username)#set 
except NoSuchElementException:
	WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID ,"login-form-username")))
	print('Username element not found.')

try:
	login_password = driver.find_element_by_id('login-form-password').send_keys(password)
except NoSuchElementExcepetion:
	print('Password element not found.')

driver.find_element_by_id('login-form-password').submit()

print('Logging in...')

time.sleep(5)

# Creating...
try:
	WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.LINK_TEXT ,"Create")))
	print('Create found...')
except NoSuchElementException:
	print('Create no found so sleeping 10seconds...')
	time.sleep(10)
	WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.LINK_TEXT ,"Create")))
	print('Create found...')
	
time.sleep(5)
driver.find_element_by_link_text('Create').click()
print('Create clicked !!')

#time.sleep(15)

print('Project field to be clicked. Waiting 60 seconds...')
try:
	WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID ,"project-field")))
except TimeoutException:
	WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.LINK_TEXT ,"Create")))
	print('Create found...')
	time.sleep(5)
	driver.find_element_by_link_text('Create').click()
	print('Create clicked !!')
	WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID ,"project-field")))

print('Element ready!')
time.sleep(5)

# Choosing project...

z = driver.find_element_by_id('project-field').click()

try:
	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT ,'Verscend DBA (VHTDBA)')))
	driver.find_element_by_link_text('Verscend DBA (VHTDBA)').click()
	print('Verscend DBA selected...')

except TimeoutException:
	time.sleep(5)
	print('verscend DBA already selected...')

'''

try:
	print('Verscend DBA to be clicked...')	
	print('10 sec...')
	time.sleep(5)
	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT ,'Verscend DBA (VHTDBA)')))
	driver.find_element_by_link_text('Verscend DBA (VHTDBA)').click()
	print('Verscend DBA Clicked !!')
except TimeoutException:
	print('verscend DBA already selected...')

time.sleep(2)
'''

# Description part

print('Filling description...')

try:
	wikiedit = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME ,"jira-wikifield")))
except TimeoutException:
	print('Next...')
	try:
		wikiedit = WebDriverWait(driver,10).until(EC.find_element_by_link_text((By.LINK_TEXT ,"Next")))
	except TimeoutException:
		driver.find_element_by_link_text('Next').click()	

	
time.sleep(10)

wikiedit = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CLASS_NAME ,"jira-wikifield")))
wikiedit = driver.find_element_by_class_name("jira-wikifield")
element = wikiedit.find_element_by_tag_name("iframe")

element.send_keys(description)




# Description part
'''
driver.find_element_by_id('mce_6_ifr').send_keys(description)


WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID ,"mce_6_ifr")))
driver.find_element_by_id('mce_6_ifr').send_keys(description)

print('keys sent')

'''
# Descritpion part

WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID ,"create-issue-submit")))
driver.find_element_by_id('create-issue-submit').text

print('create-issue-submit')




