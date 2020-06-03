import time

from selenium import webdriver  # import selenium driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  #import keys
from selenium.common.exceptions import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from getpass import getpass

import os
import sys

var_found = False
var_verscend_str = 'Verscend DBA'


var_file_path = "droplist.txt"

file = open(var_file_path,"r+")

size = os.path.getsize(var_file_path)


if size == 0:
	print('File is empty.')
	sys.exit()	
else:
	print('File is not empty. Program ongoing...')	
		


#var_description = +file.read()
#print(var_description)

var_description = 'Please drop following schemas:\n# '+file.read()

#print(file_content_list)


print(var_description)

var_username = 'i213117'
var_password = getpass('Password:\n')



def login():

	global var_password	

	print('Logging in...')	

	try:
		login_email = driver.find_element_by_id('login-form-username').send_keys(var_username) 
	except NoSuchElementException:
		WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID ,"login-form-username")))
		login_email = driver.find_element_by_id('login-form-username').send_keys(var_username)


	try:
		login_password = driver.find_element_by_id('login-form-password').send_keys(var_password)
	except NoSuchElementExcepetion:
		login_password = driver.find_element_by_id('login-form-password').send_keys(var_password)


	driver.find_element_by_id('login-form-password').submit()
	

	try:	
		WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CLASS_NAME ,"aui-message-error")))
		print('Login failed. Please re-enter your password.\n')
		var_password = getpass('Password:\n')
		login()
	except TimeoutException:
		print('Login successful...')
		return




def select_project():
	global var_found
	#global var_verscend_str

	try:
		WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.LINK_TEXT ,"Verscend DBA (VHTDBA)"))).click()
		
		#driver.find_element_by_link_text('Verscend DBA (VHTDBA)').click()
		var_found = True
		print('Verscend DBA selected...')

	except TimeoutException:
		#print(project.find_element_by_tag_name("input"))
		project.clear()
		time.sleep(0.5)
		project.click()
		project.send_keys(var_verscend_str)	
		#print('Searching for Verscend DBA (VHTDBA)...')




def check_project_field():
	try:
		WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID ,"project-field")))
		print('Project Field found...')
		return True
	except TimeoutException:
		print('Project Field not found...')
		print('Waiting...')
		time.sleep(5)
		return False
			



#description = ' Please drop following schemas:\nOE0667001SUNIL1\nOE0819001200300'

driver = webdriver.Firefox()

# base login
driver.get("https://jira2.cotiviti.com/secure/Dashboard.jspa") # get URL
time.sleep(2)


# Logging in

login()

time.sleep(2)	

# Creating...
try:
	WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.LINK_TEXT ,"Create")))
	print('Create found...')
except NoSuchElementException or TimeoutException:
	print('Create no found so sleeping 10seconds...')
	time.sleep(10)
	WebDriverWait(driver,300).until(EC.element_to_be_clickable((By.LINK_TEXT ,"Create")))
	print('Create found...')
	
time.sleep(5)
driver.find_element_by_link_text('Create').click()
print('Create clicked !!')



#time.sleep(15)

print('Project field to be clicked. Waiting 60 seconds...')

if check_project_field() == True:
	pass
else:
	check_project_field()

print('Element ready!')
#time.sleep(5)


# Choosing project...

project = driver.find_element_by_id('project-field')
project.click()


while (not var_found):
	select_project()


# Summary and Description part

print('Filling summary and description...')

try:
	wikiedit = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME ,"jira-wikifield")))
except TimeoutException:
	print('Next...')
	try:
		wikiedit = WebDriverWait(driver,30).until(EC.find_element_by_link_text((By.LINK_TEXT ,"Next")))
	except TimeoutException:
		driver.find_element_by_link_text('Next').click()	

# Delay	
time.sleep(3)


wikiedit = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID ,"summary")))
element = driver.find_element_by_id("summary")

element.click()
time.sleep(1)
element.send_keys('Schema Droplist')

time.sleep(2)

wikiedit = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CLASS_NAME ,"jira-wikifield")))
wikiedit = driver.find_element_by_class_name("jira-wikifield")
element = wikiedit.find_element_by_tag_name("iframe")

element.click()
time.sleep(2)
element.send_keys(var_description)
element.send_keys(Keys.BACKSPACE)


# Submit Part

print(WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID ,"create-issue-submit"))))

# WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID ,"create-issue-submit"))).submit()


print('create-issue-submit')

file.truncate(0)

print('file cleared !!')
