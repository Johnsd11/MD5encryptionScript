#!/bin/python
import time
import requests
import random
import hashlib
import urllib3 as ur
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import webbrowser

#http = ur.PoolManager()
#url = "http://188.166.173.208:31164/"
#response = http.request('GET', url)
#soup = bs(response.data)

def open_browser():
    driver = webdriver.Firefox()
    driver.get("http://188.166.173.208:31164/")
    #print(driver.page_source)
    return driver

def click_button(driver):
    button = driver.find_element_by_xpath("//input[@type='submit']")
    button.click()

def encrypt(driver):
    nonEncryptStr = driver.find_element_by_tag_name('h3').text
    print(nonEncryptStr)
    hash_object = hashlib.md5(nonEncryptStr.encode())
    encryptStr = hash_object.hexdigest()
    return encryptStr

def inject_encryption(driver, encryptedStr):
    textField = driver.find_element_by_name("hash")
    textField.send_keys(encryptedStr)


def main():
    driver = open_browser()
    #click_button(driver)
    encryptedStr = encrypt(driver)
    inject_encryption(driver, encryptedStr)
    click_button(driver)

main()
# <Response [200]>



