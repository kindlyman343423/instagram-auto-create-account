﻿from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import accountInfoGenerator as account
import getVerifCode as verifiCode
import fakeMail as email


browser= webdriver.Chrome("./chromedriver")
browser.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(8) #time.sleep count can be changed depending on the Internet speed.
name = account.username()

#Fill the email value
email_field = browser.find_element_by_name('emailOrPhone')
fake_email = email.getFakeMail()
email_field.send_keys(fake_email)
print(fake_email)

#Fill the fullname value
fullname_field = browser.find_element_by_name('fullName')
fullname_field.send_keys(account.generatingName())
print(account.generatingName())
#Fill username value
username_field = browser.find_element_by_name('username')
username_field.send_keys(name)
print(name)
#Fill password value
password_field  = browser.find_element_by_name('password')
password_field.send_keys('aa12345bb12345cc'+name) #You can determine another password here.
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[7]/div/button"))).click()

time.sleep(8)

#Birthday verification
browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[3]").click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select"))).click()
browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[12]").click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select"))).click()
browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[26]").click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[6]"))).click()

fMail = fake_email[0].split("@")
mailName = fMail[0]
domain =fMail[1]
instCode = verifiCode.getInstVeriCode(mailName, domain, browser)
browser.find_element_by_name('email_confirmation_code').send_keys(instCode, Keys.ENTER)


