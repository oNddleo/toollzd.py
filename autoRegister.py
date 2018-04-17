from selenium import webdriver
from openpyxl import load_workbook
from register import Register
from selenium.common.exceptions import NoSuchElementException

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
        browser.find_element_by_xpath("//div[@id='anonSignup']//a").click()

        browser.find_element_by_xpath("//div[@class='mod-input mod-login-input-email mod-input-email']//input").send_keys(element.email)
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-password mod-login-input-password mod-input-password']//input").send_keys(element.password)
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-password mod-login-input-re-password mod-input-re-password']//input").send_keys(element.password)
        browser.find_element_by_xpath("//div[@class='mod-input mod-login-input-name mod-input-name']//input").send_keys(element.name)
        register = browser.find_element_by_xpath("//div[@class='mod-login-btn']//button")
        register.click()
        try:
            browser.find_element_by_xpath("//div[@class='mod-address-book-ft']//button[@class='next-btn next-btn-warning next-btn-normal next-btn-large'").click()
        except NoSuchElementException:
            print('Error Do not button click')
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-name']//input").send_keys(element.name)
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-phone']//input").send_keys(element.phone)
        browser.find_element_by_xpath("//div[@class='mod-input mod-input-detailAddress']//input").send_keys(element.address)
        browser.find_element_by_xpath("//i[@class='next-icon next-icon-arrow-up next-icon-medium next-select-arrow']").click()
        browser.find_element_by_xpath("//div[@class='next-menu ver next-overlay-inner animated expandInDown next-select-menu next-position-tl'//li[@name=" + element.city).click()
    # print('...', email.text)
    # browser.quit()


run()
