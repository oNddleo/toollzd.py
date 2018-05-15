# -*- coding: utf-8 -*-
from selenium import webdriver
from openpyxl import load_workbook
from login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def readFile(fileName):
    wb = load_workbook(filename=fileName, read_only=True)
    ws = wb['Sheet1']
    listLogin = []

    for row in tuple(ws.rows)[1:]:
        if(row[0].value and row[1].value and row[2].value and row[3].value and row[4].value is  not None):
            register = Login(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value )
            listLogin.append(register)
    return listLogin


def run():
    listLogin = readFile('login.xlsx')
    for element in listLogin:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        link = 'https://www.lazada.vn'
        browser.get(link)
        browser.execute_script("console.log('Hello World')")
            # cookies = browser.get_cookies()
            # browser.window_handles()
            # print('...', cookies)
        browser.find_element_by_xpath("//div[@id='anonLogin']//a").click()
        browser.find_element_by_xpath("//div[@class='mod-input mod-login-input-email mod-input-email']//input").send_keys(element.email)
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-password mod-login-input-password mod-input-password']//input").send_keys(element.password)
        browser.find_element_by_xpath("//div[@class='mod-login-btn']//button").click()
        browser.get("https://member.lazada.vn/address#/book")
       
        browser.find_element_by_xpath("//button[@class='next-btn next-btn-warning next-btn-normal next-btn-large']").click()
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-name']//input").send_keys(element.name)
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-phone']//input").send_keys(element.phone)
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-detailAddress']//input").send_keys(element.address)

        time.sleep(5)



run()