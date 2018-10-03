from selenium import webdriver
from openpyxl import load_workbook
from register import Register
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
def readFile(fileName):
    wb = load_workbook(filename=fileName, read_only=True)
    ws = wb['Sheet1']
    listRegister = []

    for row in tuple(ws.rows)[1:]:
        if(row[0].value and row[1].value and row[2].value and row[3].value and row[4].value is not None):
            register = Register(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value)
            # print("register", register)
            listRegister.append(register)
    return listRegister


def run():
    listRegister = readFile('register2.xlsx')
    listArr = ["Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5", "Phường 6", "Phường 7", "Phường 8", "Phường 9", "Phường 10", "Phường 11", "Phường 12", "Phường 13", "Phường 14", "Phường 15", "Phường 16"]
    i = 0
    for element in listRegister:
        if i > 15 :
            i = 0
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        browser = webdriver.Chrome('./chromedriver',  chrome_options=chrome_options)
        link = 'https://www.lazada.vn'
        browser.get(link)
        
        # html = browser.find_element_by_xpath("//html")
        # print('...', html)
        browser.find_element_by_xpath("//div[@id='anonSignup']//a").click()
        browser.find_element_by_xpath("//div[@class='mod-input mod-login-input-email mod-input-email']//input").send_keys(element.email)
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-password mod-login-input-password mod-input-password']//input").send_keys(element.password)
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-password mod-login-input-re-password mod-input-re-password']//input").send_keys(element.password)
        browser.find_element_by_xpath("//div[@class='mod-input mod-login-input-name mod-input-name']//input").send_keys(element.name)
        browser.find_element_by_xpath("//div[@class='mod-login-btn']//button").click()
        # time.sleep(5)

        browser.get("https://member.lazada.vn/address#/book")
        browser.find_element_by_xpath("//button[@class='next-btn next-btn-warning next-btn-normal next-btn-large']").click()
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-name']//input").send_keys(element.name)
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-phone']//input").send_keys(element.phone)
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-detailAddress']//input").send_keys(element.address)
        
        arr = ["R1973756---Hồ Chí Minh", "R6846181---Quận 11", listArr[i]]
        i = i + 1
        browser.execute_script("""
            var province = arguments[0];
            var district = arguments[1];
            var ward = arguments[2];
            function run(){
                return new Promise((resolve, reject) => {
                        setTimeout(function () {
                        document.getElementsByClassName('mod-select mod-address-form-select mod-select-location-tree-1')[0].childNodes[1].click()
                        document.querySelectorAll("[value='" + province + "']")[0].click()
                        console.log('done this step 1')
                        }, 0000)
                    
                        setTimeout(function () {
                        document.getElementsByClassName('mod-select mod-address-form-select mod-select-location-tree-2')[0].childNodes[1].click()
                        document.querySelectorAll("[value='" + district + "']")[0].click()
                        console.log('done this step 2')
                        }, 1000)
                        
                        setTimeout(function () {
                        document.getElementsByClassName('mod-select mod-address-form-select mod-select-location-tree-3')[0].childNodes[1].click()
                        document.querySelectorAll("[name='" + ward + "']")[0].click()
                        console.log('done this step 3')
                        }, 2000)
                        setTimeout(function(){
                            document.getElementsByClassName('next-btn next-btn-primary next-btn-large mod-address-form-btn')[0].click();
                        }, 3000)   
                    resolve("SUCCESS")
                    })
            }
            run();
        """, arr[0], arr[1], arr[2])
        time.sleep(5)
        browser.quit()

run()
