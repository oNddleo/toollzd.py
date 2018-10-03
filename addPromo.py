# -*- coding: utf-8 -*-
from selenium import webdriver
from openpyxl import load_workbook
from login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import time


def readFile(fileName):
    wb = load_workbook(filename=fileName, read_only=True)
    ws = wb['Sheet1']
    listLogin = []

    for row in tuple(ws.rows)[1:]:
        if(row[0].value and row[1].value is not None):
            register = Login(row[0].value, row[1].value)
            listLogin.append(register)
    return listLogin


def run():
    code = 'payday20'
    for element in listLogin:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        #chrome_options.add_argument("--kiosk")
        browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        link = 'https://www.lazada.vn'
        browser.get(link)
        link = 'https://www.lazada.vn/products/xit-ngan-mui-nivea-pearl-and-beauty-spray-150ml-i150491812-s158159946.html?spm=a2o4n.searchlistbrand.list.6.1c6f3162EiY45s&search=1'

        browser.get(link)
        time.sleep(0.5)
        while True:
            try:
                browser.find_element_by_xpath("//button[@class='add-to-cart-buy-now-btn pdp-button pdp-button_type_text pdp-button_theme_orange pdp-button_size_xl']").click()
                break
            except NoSuchElementException:
                browser.refresh()
                print('element has not exist')
        time.sleep(0.5)
        link = 'https://www.lazada.vn/products/xiaomi-redmi-note-5-pro-32gb-ram-3gb-den-cuong-luc-op-lung-tai-nghe-hang-nhap-khau-i206699172-s257139450.html?spm=a2o4n.searchlist.list.11.21f37303tlOAvJ&search=1'

        browser.get(link)
        time.sleep(0.5)
        while True:
            try:
                browser.find_element_by_xpath("//button[@class='add-to-cart-buy-now-btn pdp-button pdp-button_type_text pdp-button_theme_orange pdp-button_size_xl']").click()
                break
            except NoSuchElementException:
                browser.refresh()
                print('element has not exist')
        time.sleep(0.5)
        while True:
            try:
                browser.find_element_by_xpath("//button[@class='next-btn next-btn-primary next-btn-large checkout-order-total-button automation-checkout-order-total-button-checkout']").click()
                break
            except NoSuchElementException:
                print('element checkout has not exist')
        time.sleep(0.5)
        while True:
            try:
                browser.find_element_by_xpath(
                "//input[@id='automation-voucher-input']").send_keys(code)
                break
            except NoSuchElementException:
                print('element vouncher input has not exist')
        # Lặp mã giảm giá
        while True:
            try:
            # browser.find_element_by_xpath("//button[@id='automation-voucher-input-button']").click()
                apply = browser.find_element_by_xpath(
                "//button[@id='automation-voucher-input-button']")
                ActionChains(browser).move_to_element(apply).click().perform()
            except StaleElementReferenceException:
                print('Oke dmm')
            except NoSuchElementException:
                print('element vouncher button has not exist')
                break
        time.sleep(0.5)
        # Chuyển sang hoả tốc 1 sp
        # document.getElementsByClassName('package')[1].childNodes[0].childNodes[0].childNodes[1].childNodes[0].childNodes[1].childNodes[0].childNodes[0].childNodes[0].childNodes[0].childNodes[1].childNodes[0].click()
        # browser.execute_script("""
        # function step1(){
        #     return new Promise((resolve, reject) => {
        #         setTimeout(function () {
        #              document.getElementsByClassName('next-slick-track')[0].childNodes[1].childNodes[0].click()
        #         }, 200)
        #         resolve("SUCCESS")
        #     })
        # }
        # step1();
        # """)
        
        #Chuyển sang hoả tốc 2 sp
        #  document.getElementsByClassName('package')[1].childNodes[0].childNodes[0].childNodes[1].childNodes[0].childNodes[1].childNodes[0].childNodes[0].childNodes[0].childNodes[0].childNodes[1].childNodes[0].click()
        browser.execute_script("""
        function step1(){
            return new Promise((resolve, reject) => {
                setTimeout(function () {
                            document.getElementsByClassName('package')[1].childNodes[0].childNodes[0].childNodes[1].childNodes[0].childNodes[1].childNodes[0].childNodes[0].childNodes[0].childNodes[0].childNodes[1].childNodes[0].click()
                }, 0000)
                resolve("SUCCESS")
            })
        }
        step1();
        """)
        # time.sleep(0.5)
        browser.execute_script("""
        function step1(){
            return new Promise((resolve, reject) => {
                setTimeout(function () {
                    document.getElementsByClassName('next-btn next-btn-primary next-btn-large checkout-order-total-button')[0].click()
                }, 0000)
                resolve("SUCCESS")
            })
        }
        step1();
        """)
        time.sleep(0.5)
        browser.execute_script("""
        function step2(){
            return new Promise((resolve, reject) => {
                setTimeout(function () {
                    document.getElementsByClassName('payment-method-list clearfix')[0].childNodes[0].click()
                    console.log('step2')
                }, 000)
                resolve("SUCCESS")
            })
        }
        step2();
        """)
        time.sleep(0.5)
        browser.execute_script("""
        function step2(){
            return new Promise((resolve, reject) => {
                setTimeout(function () {
                    document.getElementsByClassName('next-btn next-btn-primary next-btn-large automation-btn-place-order btn-place-order')[0].click()
                    console.log('step2')
                }, 000)
                resolve("SUCCESS")
            })
        }
        step2();
        """)
        time.sleep(10)

    browser.quit()

run()
