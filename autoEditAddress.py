
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
        if(row[0].value and row[1].value and row[2].value is  not None):
            register = Login(row[0].value, row[1].value, row[2].value )
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
        browser.find_element_by_xpath("//div[@class='next-table-cell-wrapper']//button[@class='next-btn next-btn-text next-btn-primary next-btn-medium']").click()
        # browser.find_element_by_xpath("//div[@class='mod-input mod-input-name']//input").send_keys(element.name)
        browser.find_element_by_xpath("//div[@class='mod-input floating mod-input-phone']//input").click()
        browser.execute_script("""
            function run(){
                return new Promise((resolve, reject) => {
                        setTimeout(function(){
                            document.getElementsByClassName('mod-input-close-icon')[1].click();
                        }, 0000)   
                    resolve("SUCCESS")
                    })
            }
            run();
        """)
        browser.find_element_by_xpath("//div[@class='mod-input focus error mod-input-phone']//input").send_keys(element.phone)
        # browser.find_element_by_xpath("//div[@class='mod-input floating mod-input-phone']//input").send_keys(element.phone)
        # browser.find_element_by_xpath("//div[@class='mod-input mod-input-detailAddress']//input").send_keys(element.address)
        # browser.find_element_by_xpath("//div[@class='mod-select mod-address-form-select mod-select-location-tree-1']//span[@class='next-select-inner']").click()
        # browser.execute_script("document.getElementById('R1906037').click()")
        # name = "Phường 7"
        browser.execute_script("""
            function run(){
                return new Promise((resolve, reject) => {
                        setTimeout(function(){
                            document.getElementsByClassName('next-btn next-btn-primary next-btn-large mod-address-form-btn')[0].click();
                        }, 0000)   
                    resolve("SUCCESS")
                    })
            }
            run();
        """)
        time.sleep(5)
        # print('...', browser.find_element_by_xpath("//div[@class='mod-select mod-address-form-select mod-select-location-tree-2']//span[@class='next-select-inner']").text)
        # browser.find_element_by_xpath("//div[@class='mod-select mod-address-form-select mod-select-location-tree-2']").click()
        # browser.execute_script("document.getElementById('R7154449').click()")
        # browser.find_element_by_xpath("//div[@class='mod-select mod-address-form-select mod-select-location-tree-2']//span[@class='next-select-inner']").click()
        # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "mod-select mod-address-form-select mod-select-location-tree-2"))).click()
        # browser.execute_script("document.getElementById('R7154449').click()")
        # browser.find_element_by_xpath("//div[@class='mod-select mod-address-form-select mod-select-location-tree-3']//span[@class='next-select-inner']").click()
        # browser.execute_script("document.getElementById('R80006857').click()")
        # browser.find_element_by_xpath("//div[@class='mod-address-form-action']//button[@class='next-btn next-btn-primary next-btn-large mod-address-form-btn']").click()
        
        # browser.execute_script("document.getElementById('R1906037').click()")
        # browser.execute_script("""
        #     function run(){
        #         setTimeout(function(){
        #              document.getElementsByClassName('mod-select mod-address-form-select mod-select-location-tree-2')[0].childNodes[1].click()
        #         }, 500)
        #     };
        #     run();
        # """)
        # browser.execute_script("console.log('....', document.getElementsByTagName('ul')[23])")
        # browser.execute_script("document.getElementsByTagName('ul')[23].childNodes[4].click()")
        # browser.execute_script("document.getElementById('R1906037').click()")
        # browser.find_element_by_xpath("//button[@class='next-btn next-btn-primary next-btn-large mod-address-form-btn']").click()
        # arr = browser.find_element_by_xpath("//ul[@class='next-menu-content']")
        # print('...', arr.text)
        # browser.execute_script("""
        #     function run(){
        #         setTimeout(function(){
        #              document.getElementsByClassName('mod-select mod-address-form-select mod-select-location-tree-1')[0].childNodes[1].click()
        #         }, 2000)

        #         document.getElementById('R1973756').click()
        #         console.log('dddddddddddddddddddddddddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
        #         console.log(document.getElementsByClassName('mod-select mod-address-form-select mod-select-location-tree-2')[0].childNodes[1]);
        #         setTimeout(function(){
        #              document.getElementsByClassName('mod-select mod-address-form-select mod-select-location-tree-2')[0].childNodes[1].click()
        #         }, 4000)
        #     }
        #    run();
        # """)
        
        # browser.execute_script("""document.getElementsByClassName('mod-select mod-address-form-select mod-select-location-tree-2')[0].childNodes[1].click()""")
        # browser.execute_script("document.getElementById('R7154449').click()")
        # print('html', (browser.page_source).encode('utf-8'))
        # print('...', browser.find_element_by_xpath("//div[@class='mod-select mod-address-form-select mod-select-location-tree-2']").text)
        # browser.execute_script("document.getElementById('R7154449').click()")
        # WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, "R1906037"))).click()
        # lol = browser.find_element_by_xpath("//div[@class='mod-select mod-address-form-select mod-select-location-tree-2']")
        # print('...', lol.text)
        # WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "mod-select mod-address-form-select mod-select-location-tree-2"))).click()
        # browser.find_element_by_xpath("//div[@class='mod-select mod-address-form-select mod-select-location-tree-2']").click()
        # WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID, "R7154449"))).click()
        # browser.find_element_by_xpath("//div[@class='mod-select mod-address-form-select mod-select-location-tree-3']").click()
        # WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID, "R80006857"))).click()
        # element.click()

        # html = browser.find_element_by_xpath("//html")
        # print('html', html.text)
        # browser.find_element_by_xpath("//span[@id='myAccountTrigger']").click()
        
        # browser.find_element_by_xpath("//span[@id='myAccountTrigger']").click()
        # browser.find_element_by_xpath("//a[@class='account-item-anchor']").click()
        


run()