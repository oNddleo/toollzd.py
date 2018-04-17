from selenium import webdriver
from openpyxl import load_workbook
from register import Register


def readFile(fileName):
    wb = load_workbook(filename=fileName, read_only=True)
    ws = wb['Sheet1']
    listRegister = []

    for row in tuple(ws.rows)[1:]:
        if(row[0].value and row[1].value is not None):
            register = Register(row[0].value, row[1].value, row[2].value)
            listRegister.append(register)
    return listRegister


def run():
    listRegister = readFile('register.xlsx')
    for element in listRegister:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        link = 'https://www.lazada.vn'
        browser.get(link)
        # cookies = browser.get_cookies()
        # browser.window_handles()
        # print('...', cookies)
        a = browser.find_element_by_xpath("//div[@id='anonSignup']//a").click()

        email = browser.find_element_by_xpath("//div[@class='mod-input mod-login-input-email mod-input-email']//input").send_keys(element.email)
        password = browser.find_element_by_xpath("//div[@class='mod-input mod-input-password mod-login-input-password mod-input-password']//input").send_keys(element.password)
        rePassword = browser.find_element_by_xpath("//div[@class='mod-input mod-input-password mod-login-input-re-password mod-input-re-password']//input").send_keys(element.password)
        name = browser.find_element_by_xpath("//div[@class='mod-input mod-login-input-name mod-input-name']//input").send_keys(element.name)
        register = browser.find_element_by_xpath("//div[@class='mod-login-btn']//button")
        register.click()
        
    # print('...', email.text)
    # browser.quit()


run()
