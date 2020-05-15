import time

from selenium import webdriver  # import selenium driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  #import keys
from selenium.common.exceptions import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


username = 'i213117'
password = 'Rayleigh2052#'

driver = webdriver.Firefox()

driver.get("https://jira2.cotiviti.com/secure/Dashboard.jspa") # get URL


WebDriverWait(driver,10000).until(EC.element_to_be_clickable((By.ID ,"login-form-username")))
try:
	login_email = driver.find_element_by_id('login-form-username').send_keys(username)#set 
except NoSuchElementExcepetion:
	print('Username element not found.')

try:
	login_password = driver.find_element_by_id('login-form-password').send_keys(password)
except NoSuchElementExcepetion:
	print('Password element not found.')

driver.find_element_by_id('login-form-password').submit()

print('Logging in...')

#time.sleep(300)


try:
	driver.find_element_by_link_text('Create').click()
	print('Create clicked from try block')
except NoSuchElementException:
	print('Page loading so sleeping for 30 seconds...')
	time.sleep(300)
	driver.find_element_by_link_text('Create').click()
	print('Create clicked from except block')


try:
	WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.CLASS_NAME ,"mce-content-body")))
	print('Description found !!')
except NoSuchElementException:
	print('Page loading so sleeping for 30 seconds...')
	time.sleep(300)
	WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.CLASS_NAME ,"mce-content-body")))
	print('Description found !!')

	

#WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CLASS_NAME ,"mce-content-body")))
#WebDriverWait(driver,30).until(ExpectedConditions.presenceOfElementLocated(By.CLASS_NAME ,"jira-wikifield"))
print('Filling filling...')

description = driver.find_element_by_class_name('mce-content-body')
description.send_keys(username)


#description = driver.find_element_by_class_name('rte-container')

